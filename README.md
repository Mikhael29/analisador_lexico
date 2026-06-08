# Analisador Léxico Multilinguagem

## Descrição

Este projeto consiste em um analisador léxico desenvolvido em Python com interface gráfica utilizando a biblioteca Tkinter.

O sistema permite que o usuário insira um trecho de código-fonte e realize sua análise léxica, identificando e classificando os tokens encontrados.

Além disso, o programa realiza uma detecção básica da linguagem de programação com base em palavras-chave e estruturas características de linguagens como Java, Python, JavaScript, PHP, Go, C, C++, C#, Ruby, Kotlin, Rust, Dart, Swift e TypeScript.

## Funcionalidades

* Interface gráfica simples e intuitiva.
* Identificação automática da linguagem de programação.
* Reconhecimento de palavras-chave.
* Identificação de identificadores.
* Reconhecimento de números.
* Identificação de strings.
* Reconhecimento de operadores.
* Identificação de delimitadores.

## Tecnologias Utilizadas

* Python 3
* Tkinter
* Expressões Regulares (Regex)

## Objetivo

Demonstrar o funcionamento da fase léxica de um compilador, responsável por analisar o código-fonte e transformá-lo em tokens que poderão ser utilizados nas próximas etapas do processo de compilação.

## Exemplo de Saída

```text
LINGUAGEM DETECTADA: JavaScript

TOKENS ENCONTRADOS:

function -> PALAVRA-CHAVE
saudacao -> IDENTIFICADOR
( -> DELIMITADOR
nome -> IDENTIFICADOR
) -> DELIMITADOR
```

## Como Clonar o Projeto

```bash
git clone https://github.com/Mikhael29/analisador_lexico.git
cd analisador_lexico
```

## Criando o Ambiente Virtual (venv)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Após a ativação, o terminal exibirá algo semelhante a:

```bash
(venv)
```

## Instalação das Dependências

```bash
pip install -r requirements.txt
```

## Executando o Projeto

```bash
python analisador_lexico.py
```

ou

```bash
py analisador_lexico.py
```

## Encerrando o Ambiente Virtual

```bash
deactivate
```

## Autor

Projeto desenvolvido por Mikhael Leite para a disciplina de Teoria da computação e compiladores, com o objetivo de demonstrar a implementação da fase léxica de um compilador por meio da identificação e classificação de tokens em diferentes linguagens de programação.
