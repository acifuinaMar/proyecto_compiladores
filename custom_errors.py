from dataclasses import dataclass
from enum import Enum
from typing import Optional, List
from antlr4.error.ErrorListener import ErrorListener

class ErrorType(Enum):
    """Tipos de errores del compilador"""
    LEXICO = "Error Léxico"
    SINTACTICO = "Error Sintáctico"
    SEMANTICO = "Error Semántico"
    TIPO = "Error de Tipo"
    EJECUCION = "Error de Ejecución"

@dataclass
class CompilerError:
    tipo: ErrorType
    linea: int
    columna: int
    mensaje: str
    token: Optional[str] = None
    
    def __str__(self) -> str:
        ubicacion = f"Línea {self.linea}, Columna {self.columna}"
        token_info = f" cerca de '{self.token}'" if self.token else ""
        return f"[{self.tipo.value}]{token_info} en {ubicacion}: {self.mensaje}"
    
    def to_dict(self) -> dict:
        return {
            "tipo": self.tipo.value,
            "linea": self.linea,
            "columna": self.columna,
            "mensaje": self.mensaje,
            "token": self.token
        }

class ErrorHandler:
    
    def error_ejecucion(self, linea: int, columna: int, mensaje: str, token: str = None) -> None:
        """Registra un error de ejecución"""
        error = CompilerError(ErrorType.EJECUCION, linea, columna, mensaje, token)
        self.errores.append(error)
        print(f" {error}")

    def __init__(self, detener_en_primera_falla: bool = True):
        self.errores: List[CompilerError] = []
        self.detener_en_primera_falla = detener_en_primera_falla
        self._fase_actual: Optional[str] = None
    
    def set_fase(self, nombre_fase: str):
        """Establece la fase actual para mejor reporte"""
        self._fase_actual = nombre_fase
    
    def error_lexico(self, linea: int, columna: int, mensaje: str, token: str = None) -> None:
        """Registra un error léxico"""
        error = CompilerError(ErrorType.LEXICO, linea, columna, mensaje, token)
        self.errores.append(error)
        print(f"  {error}")
    
    def error_sintactico(self, linea: int, columna: int, mensaje: str, token: str = None) -> None:
        """Registra un error sintáctico"""
        error = CompilerError(ErrorType.SINTACTICO, linea, columna, mensaje, token)
        self.errores.append(error)
        print(f"  {error}")
    
    def error_semantico(self, linea: int, columna: int, mensaje: str, token: str = None) -> None:
        """Registra un error semántico"""
        error = CompilerError(ErrorType.SEMANTICO, linea, columna, mensaje, token)
        self.errores.append(error)
        print(f"  {error}")
    
    def error_tipo(self, linea: int, columna: int, mensaje: str, token: str = None) -> None:
        """Registra un error de tipo"""
        error = CompilerError(ErrorType.TIPO, linea, columna, mensaje, token)
        self.errores.append(error)
        print(f"  {error}")
    
    def tiene_errores(self) -> bool:
        """Retorna True si hay errores registrados"""
        return len(self.errores) > 0
    
    def hay_error_grave(self) -> bool:
        """Errores léxicos o sintácticos son considerados graves"""
        for error in self.errores:
            if error.tipo in [ErrorType.LEXICO, ErrorType.SINTACTICO]:
                return True
        return False
    
    def debe_detener(self) -> bool:
        """
        Determina si el pipeline debe detenerse.
        Se detiene si hay errores graves Y está configurado para detenerse.
        """
        return self.detener_en_primera_falla and self.hay_error_grave()
    
    def limpiar(self):
        """Limpia todos los errores"""
        self.errores = []
    
    def obtener_resumen(self) -> dict:
        return {
            "total": len(self.errores),
            "lexicos": sum(1 for e in self.errores if e.tipo == ErrorType.LEXICO),
            "sintacticos": sum(1 for e in self.errores if e.tipo == ErrorType.SINTACTICO),
            "semanticos": sum(1 for e in self.errores if e.tipo == ErrorType.SEMANTICO),
            "tipos": sum(1 for e in self.errores if e.tipo == ErrorType.TIPO),
            "errores": [e.to_dict() for e in self.errores]
        }
    
    def hay_error_en_fase(self, fase: str) -> bool:
        """Verifica si hay errores en una fase específica"""
        return self.tiene_errores()


# Clase auxiliar para ANTLR
class ANTLRErrorListener(ErrorListener):
    """Adaptador para capturar errores de ANTLR"""
    
    def __init__(self, error_handler):
        super().__init__()
        self.error_handler = error_handler
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        token_text = offendingSymbol.text if offendingSymbol else None
        self.error_handler.error_sintactico(line, column, msg, token_text)
    
    # Estos métodos son necesarios para la nueva versión de ANTLR
    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass
    
    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass
    
    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass