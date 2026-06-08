import re
import tkinter as tk
from tkinter import scrolledtext

palavras_chave = [
    "if", "else", "while", "for", "print", "def", "return",
    "class", "import", "try", "except", "public", "private",
    "static", "void", "int", "float", "string", "function",
    "let", "const", "var"
]

def identificar_linguagem(codigo):
    if "System.out.println" in codigo or "public class" in codigo:
        return "Java"
    elif "def " in codigo or "import " in codigo:
        return "Python"
    elif "console.log" in codigo or "function " in codigo:
        return "JavaScript"
    elif "#include" in codigo or "printf(" in codigo:
        return "C"
    else:
        return "Linguagem não identificada"

def analisar():
    codigo = entrada.get("1.0", tk.END)

    tokens = re.findall(r"[a-zA-Z_]\w*|\d+|[+\-*/=(){};,]", codigo)

    resultado.delete("1.0", tk.END)

    linguagem = identificar_linguagem(codigo)
    resultado.insert(tk.END, f"Linguagem detectada: {linguagem}\n\n")

    resultado.insert(tk.END, "TOKENS ENCONTRADOS:\n\n")

    for token in tokens:
        if token in palavras_chave:
            categoria = "PALAVRA-CHAVE"
        elif token.isdigit():
            categoria = "NÚMERO"
        elif token in "+-*/=":
            categoria = "OPERADOR"
        elif token in "(){};,":
            categoria = "DELIMITADOR"
        else:
            categoria = "IDENTIFICADOR"

        resultado.insert(tk.END, f"{token} -> {categoria}\n")

janela = tk.Tk()
janela.title("Analisador Léxico")
janela.geometry("700x500")

tk.Label(janela, text="Digite o código:").pack()

entrada = scrolledtext.ScrolledText(janela, height=12)
entrada.pack(fill="both", expand=True)

tk.Button(janela, text="Analisar", command=analisar).pack(pady=5)

resultado = scrolledtext.ScrolledText(janela, height=12)
resultado.pack(fill="both", expand=True)

janela.mainloop()