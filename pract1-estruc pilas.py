import tkinter as tk
from tkinter import messagebox

class PilaVisual:
    def __init__(self, root):
        self.root = root
        self.root.title("Estructura de Datos: Pila (Stack) LIFO")
        self.root.geometry("650x550")
        self.root.config(padx=20, pady=20)

        # Variables de estado de la Pila
        self.capacidad_maxima = 8
        self.elementos = []
        self.tope = 0

        self.configurar_interfaz()
        self.dibujar_pila()

    def configurar_interfaz(self):
        # Frame principal para organizar los elementos
        frame_izquierdo = tk.Frame(self.root)
        frame_izquierdo.pack(side=tk.LEFT, fill=tk.Y, padx=20)

        frame_derecho = tk.Frame(self.root)
        frame_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # ---------------- FRAME IZQUIERDO: Controles ----------------
        tk.Label(frame_izquierdo, text="Control Manual", font=("Arial", 12, "bold")).pack(pady=5)
        
        self.entrada_valor = tk.Entry(frame_izquierdo, font=("Arial", 12), width=10)
        self.entrada_valor.pack(pady=5)

        tk.Button(frame_izquierdo, text="Insertar (Push)", bg="lightblue", command=self.insertar_manual).pack(fill=tk.X, pady=2)
        tk.Button(frame_izquierdo, text="Eliminar (Pop)", bg="lightcoral", command=self.eliminar_manual).pack(fill=tk.X, pady=2)

        tk.Label(frame_izquierdo, text="Controles Automáticos", font=("Arial", 12, "bold")).pack(pady=(20, 5))

        tk.Button(frame_izquierdo, text="1. Ejercicio Completo Automático", command=self.ejecutar_ejercicio_completo).pack(fill=tk.X, pady=2)
        tk.Button(frame_izquierdo, text="2. Vaciar Pila Automáticamente", command=self.vaciar_automatico).pack(fill=tk.X, pady=2)
        tk.Button(frame_izquierdo, text="3. Llenar Automáticamente", command=self.llenar_automatico).pack(fill=tk.X, pady=2)
        tk.Button(frame_izquierdo, text="4. Limpiar Todo", bg="orange", command=self.limpiar).pack(fill=tk.X, pady=(20, 2))

        # ---------------- FRAME DERECHO: Visualización ----------------
        self.label_estado = tk.Label(frame_derecho, text="TOPE: 0 | Elementos: 0/8", font=("Arial", 14, "bold"))
        self.label_estado.pack(pady=10)

        self.canvas = tk.Canvas(frame_derecho, width=200, height=400, bg="white", highlightthickness=2, highlightbackground="black")
        self.canvas.pack(pady=10)
        
        self.consola = tk.Text(frame_derecho, height=8, width=40, state=tk.DISABLED, bg="#f0f0f0")
        self.consola.pack(fill=tk.X)

    def log(self, mensaje):
        self.consola.config(state=tk.NORMAL)
        self.consola.insert(tk.END, mensaje + "\n")
        self.consola.see(tk.END)
        self.consola.config(state=tk.DISABLED)

    def dibujar_pila(self):
        self.canvas.delete("all")
        alto_celda = 400 // self.capacidad_maxima
        ancho = 200

        # Dibujar casillas vacías
        for i in range(self.capacidad_maxima):
            y1 = i * alto_celda
            y2 = y1 + alto_celda
            self.canvas.create_rectangle(0, y1, ancho, y2, outline="gray")

        # Dibujar elementos en la pila (desde abajo hacia arriba)
        for index, valor in enumerate(self.elementos):
            posicion_invertida = (self.capacidad_maxima - 1) - index
            y1 = posicion_invertida * alto_celda
            y2 = y1 + alto_celda
            
            # Resaltar la cima de la pila
            color = "lightgreen" if index == self.tope - 1 else "lightblue"
            
            self.canvas.create_rectangle(0, y1, ancho, y2, fill=color, outline="black")
            self.canvas.create_text(ancho//2, y1 + alto_celda//2, text=valor, font=("Arial", 14, "bold"))

        self.label_estado.config(text=f"TOPE: {self.tope} | Elementos: {len(self.elementos)}/{self.capacidad_maxima}")

    # ================= LOGICA LIFO =================

    def insertar_elemento(self, valor):
        if self.tope >= self.capacidad_maxima:
            messagebox.showwarning("Desbordamiento (Overflow)", f"La pila ha alcanzado su capacidad máxima de {self.capacidad_maxima}.")
            self.log(f"[Error] Overflow al intentar insertar '{valor}'")
            return False
        
        self.elementos.append(valor)
        self.tope += 1
        self.dibujar_pila()
        self.log(f"Insertar({valor}) -> TOPE: {self.tope}")
        return True

    def eliminar_elemento(self, nombre_variable="Variable"):
        if self.tope == 0:
            messagebox.showerror("Subdesbordamiento (Underflow)", "La pila está vacía. No hay elementos para extraer.")
            self.log(f"[Error] Underflow al intentar eliminar ({nombre_variable})")
            return None
        
        valor_extraido = self.elementos.pop()
        self.tope -= 1
        self.dibujar_pila()
        self.log(f"Eliminar({nombre_variable}) -> Se extrajo '{valor_extraido}'")
        return valor_extraido

    # ================= ACCIONES DE INTERFAZ =================

    def insertar_manual(self):
        valor = self.entrada_valor.get().strip()
        if not valor:
            messagebox.showinfo("Entrada Vacía", "Por favor, introduce un valor para insertar en la pila.")
            return
        if self.insertar_elemento(valor):
            self.entrada_valor.delete(0, tk.END)

    def eliminar_manual(self):
        self.eliminar_elemento("Extracción_Manual")

    def limpiar(self):
        self.elementos.clear()
        self.tope = 0
        self.dibujar_pila()
        self.consola.config(state=tk.NORMAL)
        self.consola.delete(1.0, tk.END)
        self.consola.config(state=tk.DISABLED)
        self.log("--- Pila Restablecida ---")

    # ================= CONTROLES AUTOMÁTICOS =================

    def vaciar_automatico(self):
        if self.tope > 0:
            self.eliminar_elemento("Auto")
            self.root.after(800, self.vaciar_automatico)
        else:
            self.log("La pila ha sido vaciada completamente.")

    def llenar_automatico(self):
        self.limpiar()
        # Se añaden F, G y H para alcanzar la capacidad máxima de 8
        datos_prueba = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] 
        for dato in datos_prueba:
            self.insertar_elemento(dato)
        self.log("Pila pre-llenada automáticamente a su máxima capacidad.")

    def ejecutar_ejercicio_completo(self):
        self.limpiar()
        self.log("Iniciando ejercicio del inciso A al I...")
        
        # Lista de instrucciones (operación, valor_o_variable)
        instrucciones = [
            ("insertar", "X"), # a
            ("insertar", "Y"), # b
            ("eliminar", "Z"), # c
            ("eliminar", "T"), # d
            ("eliminar", "U"), # e (Causará underflow)
            ("insertar", "V"), # f
            ("insertar", "W"), # g
            ("eliminar", "p"), # h
            ("insertar", "R")  # i
        ]
        
        self._procesar_paso(instrucciones, 0)

    def _procesar_paso(self, instrucciones, indice):
        if indice < len(instrucciones):
            operacion, argumento = instrucciones[indice]
            
            if operacion == "insertar":
                self.insertar_elemento(argumento)
            elif operacion == "eliminar":
                self.eliminar_elemento(argumento)
                
            # Programar el siguiente paso tras 1.2 segundos para visualizar el cambio
            self.root.after(1200, self._procesar_paso, instrucciones, indice + 1)
        else:
            self.log("--- Fin del Ejercicio Automático ---")

# ================= EJECUCIÓN =================
if __name__ == "__main__":
    ventana_principal = tk.Tk()
    aplicacion = PilaVisual(ventana_principal)
    ventana_principal.mainloop()