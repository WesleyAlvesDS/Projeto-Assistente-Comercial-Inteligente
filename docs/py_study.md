# Modelo de estudo em Python

Roteiro progressivo para estudar os fundamentos, praticar com exemplos pequenos e consolidar o aprendizado em um projeto.

## Índice

- [Fundamentos](#1-fundamentos)
- [Programação Orientada a Objetos](#2-programação-orientada-a-objetos)
- [Prática e revisão](#3-prática-e-revisão)
- [Exercício final](#4-exercício-final)
- [Observação final](#observação-final)

## 1. Fundamentos
### Variáveis
  - São nomes usados para armazenar valores.
  - Sintaxe básica: `nome = "Alice"`
  - Exemplo:
    ```python
    nome = "Alice"
    idade = 25
    altura = 1.72
    ativo = True
    ```

### Tipos
  - Python possui tipos como `int`, `float`, `str`, `bool`, `list` e `dict`.
  - Exemplo:
    ```python
    numero = 10          # int
    preco = 19.99        # float
    nome = "João"       # str
    aprovado = True      # bool
    itens = [1, 2, 3]    # list
    pessoa = {"nome": "Ana", "idade": 30}  # dict
    ```

### Condicionais
  - Usados para tomar decisões com `if`, `elif` e `else`.
  - Sintaxe:
    ```python
    if condicao:
        print("Verdadeiro")
    elif outra_condicao:
        print("Segunda condição")
    else:
        print("Falso")
    ```
  - Exemplo:
    ```python
    nota = 8
    if nota >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
    ```

### Loops
  - `for` percorre elementos e `while` repete enquanto a condição for verdadeira.
  - Exemplo com `for`:
    ```python
    for i in range(3):
        print(i)
    ```
  - Exemplo com `while`:
    ```python
    contador = 0
    while contador < 3:
        print(contador)
        contador += 1
    ```

### Funções
  - Permitem reutilizar trechos de código.
  - Sintaxe:
    ```python
    def nome_da_funcao(parametro):
        return parametro * 2
    ```
  - Exemplo:
    ```python
    def saudacao(nome):
        return f"Olá, {nome}!"

    print(saudacao("Maria"))
    ```

### Listas
  - São coleções ordenadas e mutáveis.
  - Sintaxe:
    ```python
    lista = [1, 2, 3]
    lista.append(4)
    ```
  - Exemplo:
    ```python
    frutas = ["maçã", "banana"]
    frutas.append("uva")
    print(frutas[0])
    ```

### Tuplas
  - São imutáveis, ou seja, não podem ser alteradas depois de criadas.
  - Sintaxe:
    ```python
    coordenada = (10, 20)
    ```
  - Exemplo:
    ```python
    ponto = (3, 5)
    print(ponto[0], ponto[1])
    ```

### Dicionários
  - Armazenam pares de chave e valor.
  - Sintaxe:
    ```python
    pessoa = {"nome": "Carlos", "idade": 28}
    ```
  - Exemplo:
    ```python
    aluno = {"nome": "Beatriz", "nota": 9.5}
    print(aluno["nome"])
    ```

### Conjuntos
  - Armazenam elementos únicos e não ordenados.
  - Sintaxe:
    ```python
    numeros = {1, 2, 3, 3}
    ```
  - Exemplo:
    ```python
    conjunto = {1, 2, 3, 4}
    conjunto.add(5)
    print(conjunto)
    ```

### Exceções
  - Tratam erros de execução com `try`, `except` e `finally`.
  - Sintaxe:
    ```python
    try:
        valor = int("abc")
    except ValueError:
        print("Erro ao converter")
    ```
  - Exemplo:
    ```python
    try:
        divisao = 10 / 0
    except ZeroDivisionError:
        print("Não é possível dividir por zero")
    ```

### Arquivos
  - Permitem ler e escrever dados em arquivos externos.
  - Sintaxe:
    ```python
    with open("arquivo.txt", "w") as arquivo:
        arquivo.write("Olá")
    ```
  - Exemplo:
    ```python
    with open("dados.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
    ```

## 2. Programação Orientada a Objetos
### Classes
  - Uma classe define um modelo ou estrutura.
  - Sintaxe:
    ```python
    class Pessoa:
        pass
    ```
  - Exemplo:
    ```python
    class Carro:
        def __init__(self, marca):
            self.marca = marca
    ```

### Objetos
  - Um objeto é uma instância de uma classe.
  - Exemplo:
    ```python
    carro = Carro("Toyota")
    print(carro.marca)
    ```

### Atributos
  - São as características do objeto.
  - Exemplo:
    ```python
    class Produto:
        def __init__(self, nome, preco):
            self.nome = nome
            self.preco = preco
    ```

### Métodos
  - São funções dentro de uma classe.
  - Exemplo:
    ```python
    class Pessoa:
        def falar(self):
            return "Olá"
    ```

### Encapsulamento
  - Restringe o acesso a partes internas do objeto.
  - Exemplo:
    ```python
    class Conta:
        def __init__(self, saldo):
            self.__saldo = saldo

        def mostrar_saldo(self):
            return self.__saldo
    ```

### Herança
  - Uma classe pode herdar características de outra.
  - Sintaxe:
    ```python
    class Animal:
        def comer(self):
            print("Comendo")

    class Cachorro(Animal):
        pass
    ```

### Composição
  - Um objeto pode conter outros objetos como parte dele.
  - Exemplo:
    ```python
    class Motor:
        pass

    class Carro:
        def __init__(self):
            self.motor = Motor()
    ```

## 3. Prática e revisão
### Resolver exercícios pequenos e progressivos
  - Comece com problemas simples e aumente a dificuldade.
  - Exemplo:
    ```python
    # Exercício 1: somar números
    total = 0
    for numero in [1, 2, 3, 4]:
        total += numero
    print(total)
    ```

### Criar mini projetos
  - Projetos como lista de tarefas, calculadora ou agenda.
  - Exemplo:
    ```python
    tarefas = ["estudar", "codar", "revisar"]
    for tarefa in tarefas:
        print(f"- {tarefa}")
    ```

### Revisar conceitos semanalmente
  - Relembre listas, funções, classes e tratamento de erros.
  - Exemplo:
    ```python
    def revisar():
        print("Revisão de Python")

    revisar()
    ```

### Reforçar pontos com anotações e exemplos
  - Documente trechos importantes e crie exemplos próprios.
  - Exemplo:
    ```python
    # Anotação: uso de dicionários
    cadastro = {"nome": "Luiz", "idade": 22}
    print(cadastro.get("nome"))
    ```

## 4. Exercício final
### Aplicar os fundamentos em um projeto simples
  - Exemplo: calculadora simples.
    ```python
    def soma(a, b):
        return a + b

    print(soma(2, 3))
    ```

### Modelar classes e objetos
  - Exemplo:
    ```python
    class Aluno:
        def __init__(self, nome, nota):
            self.nome = nome
            self.nota = nota

    aluno = Aluno("Lucas", 9.8)
    print(aluno.nome, aluno.nota)
    ```

### Testar o código e corrigir erros
  - Sempre valide entradas e depure falhas.
  - Exemplo:
    ```python
    try:
        numero = int("10")
        print(numero)
    except ValueError:
        print("Entrada inválida")
    ```

### Consolidar aprendizado com exercícios de fixação
  - Pratique repetidamente para reforçar lembrança e sintaxe.
  - Exemplo:
    ```python
    numeros = [1, 2, 3, 4, 5]
    quadrados = [n ** 2 for n in numeros]
    print(quadrados)
    ```

## Observação final
- A melhor forma de aprender Python é combinar teoria com prática.
- Sempre tente escrever pequenos trechos de código e testar o resultado em cada conceito.
- Revisar a sintaxe e os exemplos ajuda a fixar a lógica de programação.

Exemplo geral de estrutura básica em Python:
```python
# Comentário
nome = "Python"

if nome == "Python":
    print("Olá, Python!")
else:
    print("Outro nome")
```