import tkinter as tk
import mysql.connector
from tkinter import messagebox

def salvar_nome():
    nome = entry_nome.get()
    endereco = entry_endereco.get()
    if nome and endereco:
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="root",
                database="cadastro"
            )
            cursor = conexao.cursor()
            
            sql = "insert into pessoa (nome, endereco) values (%s, %s)"
            valores = (nome, endereco)
            cursor.execute(sql, valores)
            conexao.commit()
            
            label_status.config(text=f'Nome "{nome}" salvo com sucesso!', fg="green")
            entry_nome.delete(0, tk.END)
            entry_endereco.delete(0, tk.END)  # <- limpeza do campo endereço adicionada
            
            cursor.close()
            conexao.close()
        except mysql.connector.Error as erro:
            messagebox.showerror("Erro de conexão", f"Erro ao conectar ao banco:\n{erro}")
    else:
        label_status.config(text="Por favor, digite um nome.", fg="red")

root = tk.Tk()
root.title("Salvar")

largura_janela = 350
altura_janela = 200
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura_janela // 2)
por_y = (altura_tela // 2) - (altura_janela // 2)
root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{por_y}")

label_nome = tk.Label(root, text="Digite seu nome:")
label_nome.pack(pady=10)
entry_nome = tk.Entry(root, width=40)
entry_nome.pack(pady=5)

label_endereco = tk.Label(root, text="Digite seu endereco:")
label_endereco.pack(pady=10)
entry_endereco = tk.Entry(root, width=40)
entry_endereco.pack(pady=5)

botao_salvar = tk.Button(root, text="Salvar", command=salvar_nome)
botao_salvar.pack(pady=15)

label_status = tk.Label(root, text="")
label_status.pack(pady=5)

root.mainloop()
