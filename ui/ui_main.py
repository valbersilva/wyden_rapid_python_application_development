# ui_main.py

import tkinter as tk
from tkinter import messagebox

def salvar_dados():
    nome = entry_nome.get().strip()
    endereco = entry_endereco.get().strip()
    if nome and endereco:
        try:
            with open("nomes.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"Nome: {nome} | Endereço: {endereco}\n")
            messagebox.showinfo("Sucesso", f"Dados de '{nome}' salvos com sucesso!")
            entry_nome.delete(0, tk.END)
            entry_endereco.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar os dados: {e}")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha ambos os campos antes de salvar.")

def criar_ui():
    janela = tk.Tk()
    janela.title("Salvar Nomes e Endereços")

    label_nome = tk.Label(janela, text="Digite o nome:")
    label_nome.pack(pady=(10, 0))

    global entry_nome
    entry_nome = tk.Entry(janela, width=50)
    entry_nome.pack(pady=5)

    label_endereco = tk.Label(janela, text="Digite o endereço:")
    label_endereco.pack(pady=(10, 0))

    global entry_endereco
    entry_endereco = tk.Entry(janela, width=50)
    entry_endereco.pack(pady=5)

    botao_salvar = tk.Button(janela, text="Salvar Dados", command=salvar_dados)
    botao_salvar.pack(pady=15)

    janela.mainloop()

if __name__ == "__main__":
    criar_ui()
