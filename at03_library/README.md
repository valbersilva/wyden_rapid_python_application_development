# 📚 Biblioteca Digital

Projeto desenvolvido como desafio de Integração com Interface Gráfica e Banco de Dados, utilizando **Tkinter** e **SQLite**, com entrega final no dia **02 de junho**.

## 🎯 Objetivo Geral

Criar uma aplicação gráfica funcional, com menus de navegação e integração entre múltiplas tabelas relacionais, permitindo o cadastro e visualização de autores e livros. A aplicação também deve apresentar um menu de ajuda com os dados da equipe e uma descrição do projeto.

## 🧱 Tecnologias Utilizadas

* Python 3
* Tkinter (GUI)
* SQLite (Banco de dados relacional)
* Ttk.Treeview (Exibição em tabela)

## 🗃️ Estrutura do Banco de Dados

* **Tabela `autor`**

  * `id` (INTEGER, chave primária)
  * `nome` (TEXT)

* **Tabela `livro`**

  * `id` (INTEGER, chave primária)
  * `titulo` (TEXT)
  * `autor_id` (INTEGER, chave estrangeira referenciando `autor.id`)

## 📋 Funcionalidades

* Cadastro de **autores** e **livros**
* Associação de livro ao autor via chave estrangeira
* Exibição dos dados em formato de tabela (grade) com `ttk.Treeview`
* Interface gráfica amigável com **menus superiores**

  * Menu de **navegação entre módulos**: Autores, Livros
  * Menu de **ajuda** com nome dos integrantes e descrição do projeto

## 🎮 Como executar o projeto

1. Certifique-se de ter o Python 3 instalado.
2. Execute o script com o seguinte comando:

```bash
python3 biblioteca.py
```

3. A aplicação abrirá automaticamente e o banco de dados `biblioteca.db` será criado na primeira execução.

## 👥 Integrantes do Grupo

* Valber Silva
> Obs: Substitua os nomes acima pelos nomes reais da equipe.

## 📝 Título do Projeto

**Biblioteca Digital**

## 🧾 Descrição da Aplicação

Sistema simples para gestão de autores e seus respectivos livros. Os dados podem ser inseridos via formulários e são exibidos em tabelas interativas. O projeto visa demonstrar o uso integrado de uma interface gráfica com um banco de dados relacional utilizando Python.

## ✅ Requisitos atendidos

* [x] Interface gráfica com Tkinter
* [x] Banco de dados SQLite
* [x] Tabelas relacionadas com chave estrangeira
* [x] Cadastro via formulário
* [x] Visualização em grade com Treeview
* [x] Menu de navegação e ajuda com créditos

---

Desenvolvido como parte da disciplina de Programação da Faculdade.
