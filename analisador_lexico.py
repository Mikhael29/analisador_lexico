import re
import tkinter as tk
from tkinter import scrolledtext

palavras_chave = [
    "if", "else", "while", "for", "print", "def", "return",
    "class", "import", "try", "except", "public", "private",
    "static", "void", "int", "float", "double", "char",
    "string", "function", "let", "const", "var",
    "package", "main", "using", "namespace", "new",
    "switch", "case", "break", "continue", "echo",
    "puts", "fn", "struct", "interface", "type",
    "boolean", "true", "false", "null"
]

def identificar_linguagem(codigo):

    codigo_lower = codigo.lower()

    # Java
    if "system.out.println" in codigo_lower or "public class" in codigo_lower:
        return "Java"

    # Python
    elif "def " in codigo_lower or "import " in codigo_lower:
        return "Python"

    # JavaScript
    elif "console.log" in codigo_lower or "function " in codigo_lower:
        return "JavaScript"

    # TypeScript
    elif "interface " in codigo_lower or "type " in codigo_lower:
        return "TypeScript"

    # C
    elif "#include" in codigo_lower or "printf(" in codigo_lower:
        return "C"

    # C++
    elif "#include <iostream>" in codigo_lower or "cout <<" in codigo_lower:
        return "C++"

    # C#
    elif "console.writeline" in codigo_lower or "using system;" in codigo_lower:
        return "C#"

    # PHP
    elif "<?php" in codigo_lower or "echo " in codigo_lower:
        return "PHP"

    # Go
    elif "package main" in codigo_lower or "fmt.println" in codigo_lower:
        return "Go"

    # Ruby
    elif "puts " in codigo_lower:
        return "Ruby"

    # Kotlin
    elif "fun main" in codigo_lower:
        return "Kotlin"

    # Rust
    elif "fn main()" in codigo_lower or "println!" in codigo_lower:
        return "Rust"

    # Dart
    elif "void main()" in codigo_lower and "print(" in codigo_lower:
        return "Dart"

    # Swift
    elif "import swift" in codigo_lower:
        return "Swift"

    else:
        return "Linguagem não identificada"

def analisar():
    codigo = entrada.get("1.0", tk.END)

    tokens = re.findall(
        r"[a-zA-Z_]\w*|\d+|\".*?\"|'.*?'|[+\-*/=(){};,.<>]",
        codigo
    )

    resultado.delete("1.0", tk.END)

    linguagem = identificar_linguagem(codigo)

    resultado.insert(
        tk.END,
        f"LINGUAGEM DETECTADA: {linguagem}\n\n"
    )

    resultado.insert(tk.END, "TOKENS ENCONTRADOS:\n\n")

    for token in tokens:

        if token in palavras_chave:
            categoria = "PALAVRA-CHAVE"

        elif token.isdigit():
            categoria = "NÚMERO"

        elif token.startswith('"') or token.startswith("'"):
            categoria = "STRING"

        elif token in "+-*/=<>" :
            categoria = "OPERADOR"

        elif token in "(){};,.":
            categoria = "DELIMITADOR"

        else:
            categoria = "IDENTIFICADOR"

        resultado.insert(
            tk.END,
            f"{token} -> {categoria}\n"
        )

janela = tk.Tk()
janela.title("Analisador Léxico")
janela.geometry("800x600")

titulo = tk.Label(
    janela,
    text="Analisador Léxico",
    font=("Arial", 14, "bold")
)
titulo.pack(pady=5)

tk.Label(
    janela,
    text="Cole o código abaixo:"
).pack()

entrada = scrolledtext.ScrolledText(
    janela,
    height=15
)
entrada.pack(fill="both", expand=True, padx=10)

tk.Button(
    janela,
    text="Analisar",
    command=analisar
).pack(pady=10)

resultado = scrolledtext.ScrolledText(
    janela,
    height=15
)
resultado.pack(fill="both", expand=True, padx=10)

janela.mainloop()