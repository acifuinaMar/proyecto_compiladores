from typing import Dict, List, Optional, Any, Set
from dataclasses import dataclass, field
from enum import Enum

class SimboloTipo(Enum):
    """Tipos de símbolos que puede almacenar la tabla"""
    VARIABLE = "variable"
    FUNCION = "funcion"
    PARAMETRO = "parametro"
    ARRAY = "array"

class TipoDato(Enum):
    """Tipos de datos soportados"""
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"
    STRING = "string"
    VOID = "void"
    INDEFINIDO = "indefinido"
    
    @classmethod
    def desde_string(cls, s: str):
        """Convierte string a TipoDato"""
        mapping = {
            "int": cls.INT,
            "float": cls.FLOAT,
            "bool": cls.BOOL,
            "string": cls.STRING,
            "void": cls.VOID
        }
        return mapping.get(s, cls.INDEFINIDO)

@dataclass
class Simbolo:
    """Representa un símbolo en la tabla"""
    nombre: str
    tipo: SimboloTipo
    tipo_dato: TipoDato
    linea_decl: int
    columna_decl: int
    valor: Any = None
    parametros: List['Simbolo'] = field(default_factory=list)  # Para funciones
    dimensiones: Optional[int] = None  # Para arrays
    
    def __str__(self) -> str:
        base = f"{self.nombre} : {self.tipo_dato.value} ({self.tipo.value})"
        if self.parametros:
            params = ", ".join([f"{p.nombre}:{p.tipo_dato.value}" for p in self.parametros])
            base += f"({params})"
        return base

class Scope:
    def __init__(self, nombre: str = "global", es_funcion: bool = False):
        self.nombre = nombre
        self.es_funcion = es_funcion
        self.simbolos: Dict[str, Simbolo] = {}
        self.parent: Optional['Scope'] = None
        self.tipo_retorno: Optional[TipoDato] = None  # Solo si es_funcion=True
    
    def definir(self, simbolo: Simbolo) -> bool:
        if simbolo.nombre in self.simbolos:
            return False  # Ya existe
        self.simbolos[simbolo.nombre] = simbolo
        return True
    
    def buscar(self, nombre: str) -> Optional[Simbolo]:
        return self.simbolos.get(nombre)
    
    def existe_local(self, nombre: str) -> bool:
        """Verifica si existe en el scope actual"""
        return nombre in self.simbolos
    
    def __str__(self) -> str:
        return f"Scope({self.nombre}, {len(self.simbolos)} símbolos)"

class SymbolTable:
    
    def __init__(self):
        self.scopes: List[Scope] = []
        self._push_scope("global")
    
    def _push_scope(self, nombre: str, es_funcion: bool = False) -> Scope:
        nuevo_scope = Scope(nombre, es_funcion)
        if self.scopes:
            nuevo_scope.parent = self.scopes[-1]
        self.scopes.append(nuevo_scope)
        return nuevo_scope
    
    def push_scope(self, nombre: str = "bloque") -> Scope:
        return self._push_scope(nombre, es_funcion=False)
    
    def push_function_scope(self, nombre: str, tipo_retorno: TipoDato) -> Scope:
        scope = self._push_scope(nombre, es_funcion=True)
        scope.tipo_retorno = tipo_retorno
        return scope
    
    def pop_scope(self) -> Optional[Scope]:
        if len(self.scopes) > 1:  # Nunca eliminar el scope global
            return self.scopes.pop()
        return None
    
    def scope_actual(self) -> Scope:
        return self.scopes[-1]
    
    def scope_global(self) -> Scope:
        return self.scopes[0]
    
    def definir_variable(self, nombre: str, tipo_dato: TipoDato, 
                         linea: int, columna: int, valor: Any = None) -> bool:
        simbolo = Simbolo(
            nombre=nombre,
            tipo=SimboloTipo.VARIABLE,
            tipo_dato=tipo_dato,
            linea_decl=linea,
            columna_decl=columna,
            valor=valor
        )
        return self.scope_actual().definir(simbolo)
    
    def definir_parametro(self, nombre: str, tipo_dato: TipoDato,
                          linea: int, columna: int) -> bool:
        simbolo = Simbolo(
            nombre=nombre,
            tipo=SimboloTipo.PARAMETRO,
            tipo_dato=tipo_dato,
            linea_decl=linea,
            columna_decl=columna
        )
        return self.scope_actual().definir(simbolo)
    
    def definir_funcion(self, nombre: str, tipo_retorno: TipoDato,
                        parametros: List[Simbolo], linea: int, columna: int) -> bool:
                # Las funciones solo se definen en el scope global
        simbolo = Simbolo(
            nombre=nombre,
            tipo=SimboloTipo.FUNCION,
            tipo_dato=tipo_retorno,
            linea_decl=linea,
            columna_decl=columna,
            parametros=parametros
        )
        return self.scope_global().definir(simbolo)
    
    def buscar(self, nombre: str, buscar_en_scopes: bool = True) -> Optional[Simbolo]:
        # Comenzar desde el scope actual
        scope = self.scope_actual()
        
        while scope:
            simbolo = scope.buscar(nombre)
            if simbolo:
                return simbolo
            if not buscar_en_scopes:
                break
            scope = scope.parent
        
        return None
    
    def buscar_en_scope_actual(self, nombre: str) -> Optional[Simbolo]:
        return self.scope_actual().buscar(nombre)
    
    def buscar_funcion(self, nombre: str) -> Optional[Simbolo]:
        simbolo = self.scope_global().buscar(nombre)
        if simbolo and simbolo.tipo == SimboloTipo.FUNCION:
            return simbolo
        return None
    
    def obtener_tipo(self, nombre: str) -> Optional[TipoDato]:
        simbolo = self.buscar(nombre)
        return simbolo.tipo_dato if simbolo else None
    
    def esta_declarado(self, nombre: str) -> bool:
        return self.buscar(nombre) is not None
    
    def esta_declarado_local(self, nombre: str) -> bool:
        return self.scope_actual().existe_local(nombre)
    
    def obtener_valor(self, nombre: str) -> Any:
        simbolo = self.buscar(nombre)
        return simbolo.valor if simbolo else None
    
    def asignar_valor(self, nombre: str, valor: Any, linea: int, columna: int) -> bool:
        simbolo = self.buscar(nombre)
        if not simbolo:
            return False
        
        # Validar tipo (básica)
        tipo_esperado = simbolo.tipo_dato
        tipo_valor = self._tipo_de_valor(valor)
        
        if tipo_esperado != tipo_valor:
            # Permitir int -> float
            if not (tipo_esperado == TipoDato.FLOAT and tipo_valor == TipoDato.INT):
                raise TypeError(f"Tipo incorrecto: esperaba {tipo_esperado.value}, recibió {tipo_valor.value}")
        
        simbolo.valor = valor
        return True
    
    def _tipo_de_valor(self, valor: Any) -> TipoDato:
        if isinstance(valor, int):
            return TipoDato.INT
        elif isinstance(valor, float):
            return TipoDato.FLOAT
        elif isinstance(valor, str):
            return TipoDato.STRING
        elif isinstance(valor, bool):
            return TipoDato.BOOL
        return TipoDato.INDEFINIDO
    
    def en_ambito_funcion(self) -> bool:
        for scope in reversed(self.scopes):
            if scope.es_funcion:
                return True
        return False
    
    def obtener_funcion_actual(self) -> Optional[Scope]:
        for scope in reversed(self.scopes):
            if scope.es_funcion:
                return scope
        return None
    
    def imprimir(self, mostrar_valores: bool = False):
        """Depuración: imprime la tabla de símbolos"""
        print("\n" + "="*60)
        print("TABLA DE SÍMBOLOS")
        print("="*60)
        for i, scope in enumerate(self.scopes):
            indent = "  " * i
            print(f"{indent}[{scope.nombre}]")
            for nombre, sim in scope.simbolos.items():
                valor_str = f" = {sim.valor}" if mostrar_valores and sim.valor is not None else ""
                print(f"{indent}  ├─ {sim}{valor_str}")
    
    def limpiar(self):
        """Limpia la tabla"""
        self.scopes = []
        self._push_scope("global")