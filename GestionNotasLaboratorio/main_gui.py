import tkinter as tk
from tkinter import ttk, messagebox
import logica


class AplicacionNotasLaboratorio:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sistema de Gestión de Notas de Laboratorio")
        self.ventana.geometry("800x600")
        self.ventana.config(bg="#f0f0f0")
        
        self.crear_interfaz()
        self.actualizar_lista_notas()
    
    def crear_interfaz(self):
        frame_titulo = tk.Frame(self.ventana, bg="#2c3e50", pady=15)
        frame_titulo.pack(fill=tk.X)
        
        tk.Label(
            frame_titulo,
            text="📝 Gestión de Notas de Laboratorio",
            font=("Arial", 18, "bold"),
            bg="#2c3e50",
            fg="white"
        ).pack()
        
        frame_agregar = tk.LabelFrame(
            self.ventana,
            text="Agregar Nueva Nota",
            font=("Arial", 12, "bold"),
            bg="#ecf0f1",
            padx=10,
            pady=10
        )
        frame_agregar.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(
            frame_agregar,
            text="Título:",
            font=("Arial", 10, "bold"),
            bg="#ecf0f1"
        ).grid(row=0, column=0, sticky="w", pady=5)
        
        self.entrada_titulo = tk.Entry(frame_agregar, width=50, font=("Arial", 10))
        self.entrada_titulo.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(
            frame_agregar,
            text="Descripción:",
            font=("Arial", 10, "bold"),
            bg="#ecf0f1"
        ).grid(row=1, column=0, sticky="nw", pady=5)
        
        self.entrada_descripcion = tk.Text(
            frame_agregar,
            width=50,
            height=4,
            font=("Arial", 10)
        )
        self.entrada_descripcion.grid(row=1, column=1, padx=10, pady=5)
        
        self.boton_agregar = tk.Button(
            frame_agregar,
            text="➕ Agregar Nota",
            command=self.agregar_nota,
            bg="#27ae60",
            fg="white",
            font=("Arial", 11, "bold"),
            cursor="hand2",
            padx=20,
            pady=5
        )
        self.boton_agregar.grid(row=2, column=1, sticky="e", pady=10)
        
        frame_busqueda = tk.Frame(self.ventana, bg="#f0f0f0")
        frame_busqueda.pack(fill=tk.X, padx=20, pady=5)
        
        tk.Label(
            frame_busqueda,
            text="🔍 Buscar:",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0"
        ).pack(side=tk.LEFT, padx=5)
        
        self.entrada_busqueda = tk.Entry(
            frame_busqueda,
            width=40,
            font=("Arial", 10)
        )
        self.entrada_busqueda.pack(side=tk.LEFT, padx=5)
        self.entrada_busqueda.bind("<KeyRelease>", lambda e: self.buscar_notas())
        
        tk.Button(
            frame_busqueda,
            text="Limpiar",
            command=self.limpiar_busqueda,
            bg="#95a5a6",
            fg="white",
            font=("Arial", 9, "bold"),
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)
        
        self.label_contador = tk.Label(
            frame_busqueda,
            text="Total: 0 notas",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0",
            fg="#34495e"
        )
        self.label_contador.pack(side=tk.RIGHT, padx=10)
        
        frame_lista = tk.LabelFrame(
            self.ventana,
            text="Lista de Notas Guardadas",
            font=("Arial", 12, "bold"),
            bg="#ecf0f1",
            padx=10,
            pady=10
        )
        frame_lista.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        scrollbar = ttk.Scrollbar(frame_lista)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree = ttk.Treeview(
            frame_lista,
            columns=("ID", "Titulo", "Descripcion"),
            show="headings",
            yscrollcommand=scrollbar.set,
            height=10
        )
        
        self.tree.heading("ID", text="ID")
        self.tree.heading("Titulo", text="Título")
        self.tree.heading("Descripcion", text="Descripción")
        
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Titulo", width=200, anchor="w")
        self.tree.column("Descripcion", width=450, anchor="w")
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.tree.yview)
        
        frame_botones = tk.Frame(self.ventana, bg="#f0f0f0")
        frame_botones.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Button(
            frame_botones,
            text="🗑️ Eliminar Seleccionada",
            command=self.eliminar_nota,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            padx=15,
            pady=5
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            frame_botones,
            text="🔄 Actualizar Lista",
            command=self.actualizar_lista_notas,
            bg="#3498db",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            padx=15,
            pady=5
        ).pack(side=tk.LEFT, padx=5)
    
    def agregar_nota(self):
        titulo = self.entrada_titulo.get().strip()
        descripcion = self.entrada_descripcion.get("1.0", tk.END).strip()
        
        if not titulo or not descripcion:
            messagebox.showwarning(
                "Campos vacíos",
                "Por favor, completa el título y la descripción."
            )
            return
        
        logica.agregar_nota(titulo, descripcion)
        
        self.entrada_titulo.delete(0, tk.END)
        self.entrada_descripcion.delete("1.0", tk.END)
        
        self.actualizar_lista_notas()
        
        messagebox.showinfo("Éxito", "¡Nota agregada correctamente!")
    
    def actualizar_lista_notas(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        notas = logica.obtener_todas_notas()
        
        for nota in notas:
            self.tree.insert(
                "",
                tk.END,
                values=(nota["id"], nota["titulo"], nota["descripcion"])
            )
        
        self.label_contador.config(text=f"Total: {logica.contar_notas()} notas")
    
    def buscar_notas(self):
        termino = self.entrada_busqueda.get().strip()
        
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        notas_filtradas = logica.buscar_notas(termino)
        
        for nota in notas_filtradas:
            self.tree.insert(
                "",
                tk.END,
                values=(nota["id"], nota["titulo"], nota["descripcion"])
            )
        
        self.label_contador.config(text=f"Encontradas: {len(notas_filtradas)} notas")
    
    def limpiar_busqueda(self):
        self.entrada_busqueda.delete(0, tk.END)
        self.actualizar_lista_notas()
    
    def eliminar_nota(self):
        seleccion = self.tree.selection()
        
        if not seleccion:
            messagebox.showwarning(
                "Sin selección",
                "Por favor, selecciona una nota para eliminar."
            )
            return
        
        item = self.tree.item(seleccion[0])
        nota_id = item["values"][0]
        
        respuesta = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Estás seguro de eliminar la nota ID {nota_id}?"
        )
        
        if respuesta:
            logica.eliminar_nota(nota_id)
            self.actualizar_lista_notas()
            messagebox.showinfo("Éxito", "Nota eliminada correctamente.")


def main():
    ventana = tk.Tk()
    app = AplicacionNotasLaboratorio(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()