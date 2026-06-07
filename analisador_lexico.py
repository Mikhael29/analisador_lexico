import re

# Palavras-chave da linguagem
palavras_chave = ["if", "else", "while", "for", "print"]

def analise_lexica(codigo):
    tokens = re.findall(r"[a-zA-Z_]\w*|\d+|[+\-*/=(){};,]", codigo)

    print("\nTOKENS ENCONTRADOS:")
    
    for token in tokens:
        if token in palavras_chave:
            print(f"{token} -> PALAVRA-CHAVE")
        elif token.isdigit():
            print(f"{token} -> NÚMERO")
        elif token in "+-*/=":
            print(f"{token} -> OPERADOR")
        elif token in "(){};,":
            print(f"{token} -> DELIMITADOR")
        else:
            print(f"{token} -> IDENTIFICADOR")

print("=== ANALISADOR LÉXICO ===")

codigo = input("Digite um código: ")

analise_lexica(codigo)




