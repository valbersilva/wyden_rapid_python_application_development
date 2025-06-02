import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Conexão com o banco de dados SQLite
conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

# Criação das tabelas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS autor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS livro (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor_id INTEGER NOT NULL,
        FOREIGN KEY (autor_id) REFERENCES autor(id)
    )
""")

conn.commit()

class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Biblioteca")

        self.menu = tk.Menu(root)
        root.config(menu=self.menu)

        self.menu.add_command(label="Autores", command=self.abrir_tela_autores)
        self.menu.add_command(label="Livros", command=self.abrir_tela_livros)
        self.menu.add_command(label="Ajuda", command=self.abrir_ajuda)

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)
        self.abrir_tela_autores()

    def limpar_tela(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def abrir_tela_autores(self):
        self.limpar_tela()
        tk.Label(self.frame, text="Cadastro de Autor").grid(row=0, column=0, columnspan=2)
        tk.Label(self.frame, text="Nome:").grid(row=1, column=0)
        nome_entry = tk.Entry(self.frame)
        nome_entry.grid(row=1, column=1)

        def salvar_autor():
            nome = nome_entry.get()
            if nome:
                cursor.execute("INSERT INTO autor (nome) VALUES (?)", (nome,))
                conn.commit()
                messagebox.showinfo("Sucesso", "Autor cadastrado com sucesso!")
                mostrar_autores()
                nome_entry.delete(0, tk.END)

        tk.Button(self.frame, text="Salvar", command=salvar_autor).grid(row=2, column=0, columnspan=2, pady=5)

        tree = ttk.Treeview(self.frame, columns=("ID", "Nome"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Nome", text="Nome")
        tree.grid(row=3, column=0, columnspan=2)

        def mostrar_autores():
            for row in tree.get_children():
                tree.delete(row)
            cursor.execute("SELECT * FROM autor")
            for autor in cursor.fetchall():
                tree.insert("", "end", values=autor)

        mostrar_autores()

    def abrir_tela_livros(self):
        self.limpar_tela()
        tk.Label(self.frame, text="Cadastro de Livro").grid(row=0, column=0, columnspan=2)
        tk.Label(self.frame, text="Título:").grid(row=1, column=0)
        titulo_entry = tk.Entry(self.frame)
        titulo_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Autor:").grid(row=2, column=0)
        autores_combo = ttk.Combobox(self.frame, state="readonly")
        autores_combo.grid(row=2, column=1)

        def carregar_autores():
            cursor.execute("SELECT id, nome FROM autor")
            autores = cursor.fetchall()
            autores_combo["values"] = [f"{id} - {nome}" for id, nome in autores]

        carregar_autores()

        def salvar_livro():
            titulo = titulo_entry.get()
            autor_info = autores_combo.get()
            if titulo and autor_info:
                autor_id = int(autor_info.split(" - ")[0])
                cursor.execute("INSERT INTO livro (titulo, autor_id) VALUES (?, ?)", (titulo, autor_id))
                conn.commit()
                messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")
                mostrar_livros()
                titulo_entry.delete(0, tk.END)

        tk.Button(self.frame, text="Salvar", command=salvar_livro).grid(row=3, column=0, columnspan=2, pady=5)

        tree = ttk.Treeview(self.frame, columns=("ID", "Título", "Autor"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Título", text="Título")
        tree.heading("Autor", text="Autor")
        tree.grid(row=4, column=0, columnspan=2)

        def mostrar_livros():
            for row in tree.get_children():
                tree.delete(row)
            cursor.execute("""
                SELECT livro.id, livro.titulo, autor.nome 
                FROM livro 
                JOIN autor ON livro.autor_id = autor.id
            """)
            for livro in cursor.fetchall():
                tree.insert("", "end", values=livro)

        mostrar_livros()

    def abrir_ajuda(self):
        self.limpar_tela()
        tk.Label(self.frame, text="Ajuda", font=("Arial", 14, "bold")).pack(pady=5)
        tk.Label(self.frame, text="Integrantes do Grupo:").pack(anchor="w")
        tk.Label(self.frame, text="- Aluno 1 (ex: Valber Silva)").pack(anchor="w")
        tk.Label(self.frame, text="\nBiblioteca Digital").pack(anchor="w")
        tk.Label(self.frame, text="Descrição:").pack(anchor="w")
        tk.Label(self.frame, text="Sistema para cadastro e visualização de autores e seus respectivos livros.").pack(anchor="w")

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()