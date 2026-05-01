import tkinter as tk
from tkinter import scrolledtext, ttk, messagebox
import io
import subprocess
from contextlib import redirect_stdout

from pipeline import Pipeline
from ir_generator import IRGenerator
from custom_errors import ErrorHandler

class CompiladorProIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("Compiladores Proyecto 3")
        self.root.geometry("1000x750")
        self.root.configure(bg="#f5f6f7")
        
        #ESTILOS
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=25)
        style.configure("TNotebook.Tab", font=("Segoe UI", 9), padding=[10, 5])

        #CONTENEDOR PRINCIPAL
        main_frame = tk.Frame(self.root, bg="#f5f6f7")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        #LADO IZQUIERDO (Editor y Tabla)
        left_frame = tk.Frame(main_frame, bg="#f5f6f7")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        tk.Label(left_frame, text="EDITOR DE CÓDIGO FUENTE", bg="#f5f6f7", font=("Segoe UI", 10, "bold")).pack(anchor="w")
        
        self.editor = scrolledtext.ScrolledText(left_frame, font=("Consolas", 12), undo=True, 
                                               bg="white", fg="#2d3436", insertbackground="black")
        self.editor.pack(fill=tk.BOTH, expand=True, pady=(5, 10))

        # Botones 
        btn_frame = tk.Frame(left_frame, bg="#f5f6f7")
        btn_frame.pack(fill=tk.X, pady=5)

        self.btn_run = tk.Button(btn_frame, text="▶ EJECUTAR", bg="#2ecc71", fg="white", 
                                 font=("Segoe UI", 10, "bold"), relief="flat", padx=20, pady=8,
                                 command=self.run_pipeline)
        self.btn_run.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        self.btn_clear = tk.Button(btn_frame, text="🗑 LIMPIAR", bg="#ecf0f1", fg="#2d3436", 
                                   font=("Segoe UI", 10), relief="flat", padx=20, pady=8,
                                   command=self.clear_all)
        self.btn_clear.pack(side=tk.LEFT)

        # Tabla de Tiempos
        tk.Label(left_frame, text="ESTADO DEL PIPELINE", bg="#f5f6f7", font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(10, 0))
        self.tree = ttk.Treeview(left_frame, columns=("Fase", "Resultado", "Tiempo"), show='headings', height=6)
        self.tree.heading("Fase", text="FASE")
        self.tree.heading("Resultado", text="RESULTADO")
        self.tree.heading("Tiempo", text="TIEMPO (MS)")
        self.tree.column("Fase", width=150)
        self.tree.column("Resultado", width=100, anchor="center")
        self.tree.column("Tiempo", width=100, anchor="center")
        self.tree.pack(fill=tk.X, pady=5)

        # LADO DERECHO (Pestañas de Resultados)
        right_frame = tk.Frame(main_frame, bg="#f5f6f7")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))

        tk.Label(right_frame, text="SALIDAS Y GENERACIÓN", bg="#f5f6f7", font=("Segoe UI", 10, "bold")).pack(anchor="w")
        
        self.tabs = ttk.Notebook(right_frame)
        self.tabs.pack(fill=tk.BOTH, expand=True, pady=5)

        # Creación de pestañas
        self.txt_console = self.create_tab("Consola")
        self.txt_tac = self.create_tab("TAC")
        self.txt_ir = self.create_tab("LLVM IR")
        self.txt_exec = self.create_tab("Ejecución (lli)")
        self.txt_errors = self.create_tab("Errores")

    def create_tab(self, name):
        frame = tk.Frame(self.tabs, bg="black")
        self.tabs.add(frame, text=name)
        text_area = scrolledtext.ScrolledText(frame, bg="#1e1e1e", fg="#dcdcdc", 
                                             insertbackground="white", font=("Consolas", 10))
        text_area.pack(fill=tk.BOTH, expand=True)
        return text_area

    def clear_all(self):
        self.tree.delete(*self.tree.get_children())
        for area in [self.txt_console, self.txt_tac, self.txt_ir, self.txt_exec, self.txt_errors]:
            area.delete('1.0', tk.END)

    def update_tab(self, widget, content):
        widget.delete('1.0', tk.END)
        widget.insert(tk.END, content)

    def run_pipeline(self):
        self.clear_all()
        source_code = self.editor.get("1.0", tk.END)
        
        pipeline = Pipeline()
        output_buffer = io.StringIO()

        try:
            # Captura de salida estándar (prints del Visitor)
            with redirect_stdout(output_buffer):
                self.update_tab(self.txt_console, "Iniciando Pipeline\n")
                success = pipeline.ejecutar(source_code)
            
            self.update_tab(self.txt_console, output_buffer.getvalue())

            # Llenar tabla de tiempos
            for fase, data in pipeline.resultados.items():
                status = "OK" if data["exitoso"] else "ERROR"
                self.tree.insert("", tk.END, values=(fase.upper(), status, f"{data['tiempo_ms']:.2f}"))

            # Manejo de Errores
            if pipeline.error_handler.tiene_errores():
                error_msg = "\n".join([str(err) for err in pipeline.error_handler.errores])
                self.update_tab(self.txt_errors, error_msg)
                self.tabs.select(4) # Salta a pestaña errores
                return

            if success:
                # Mostrar TAC
                try:
                    with open("salida.tac", "r", encoding='utf-8') as f:
                        self.update_tab(self.txt_tac, f.read())
                except FileNotFoundError:
                    self.update_tab(self.txt_tac, "Error: salida.tac no generado.")

                # Generar LLVM IR
                ir_gen = IRGenerator()
                llvm_code = ir_gen.visit(pipeline.ast)
                self.update_tab(self.txt_ir, llvm_code)
                
                with open("salida.ll", "w", encoding='utf-8') as f_ir:
                    f_ir.write(llvm_code)

                # Ejecutar con lli
                try:
                    result = subprocess.run(["lli", "salida.ll"], capture_output=True, text=True, timeout=5)
                    output = f"SALIDA LLI:\n{result.stdout}\n{'-'*20}\nERRORES LLI:\n{result.stderr}"
                    self.update_tab(self.txt_exec, output)
                except Exception as e:
                    self.update_tab(self.txt_exec, f"Error ejecutando lli: {str(e)}")

        except Exception as e:
            messagebox.showerror("Excepción Crítica", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = CompiladorProIDE(root)
    root.mainloop()