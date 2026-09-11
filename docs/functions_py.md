# Funções integradas do Python

## Conversão e representação de dados

| Função | Descrição | Exemplo |
|---|---|---|
| `abs()` | Valor absoluto de um número | `abs(-7)  # 7` |
| `bin()` | Converte inteiro para string binária | `bin(10)  # '0b1010'` |
| `bool()` | Converte para valor booleano | `bool(0)  # False` |
| `bytes()` | Cria objeto `bytes` (imutável) | `bytes([65, 66])  # b'AB'` |
| `bytearray()` | Cria objeto `bytearray` (mutável) | `bytearray('AB', 'ascii')` |
| `chr()` | Retorna o caractere para um código Unicode | `chr(65)  # 'A'` |
| `complex()` | Cria um número complexo | `complex(2, 3)  # (2+3j)` |
| `dict()` | Cria um dicionário | `dict(nome='Ana', idade=25)` |
| `float()` | Converte para número de ponto flutuante | `float('3.14')  # 3.14` |
| `frozenset()` | Cria um conjunto imutável | `frozenset({1, 2, 2})  # frozenset({1, 2})` |
| `int()` | Converte para inteiro | `int('42')  # 42` |
| `list()` | Cria uma lista | `list('abc')  # ['a', 'b', 'c']` |
| `ord()` | Retorna o código Unicode de um caractere | `ord('A')  # 65` |
| `set()` | Cria um conjunto | `set([1, 2, 2])  # {1, 2}` |
| `str()` | Converte para string | `str(123)  # '123'` |
| `tuple()` | Cria uma tupla | `tuple([1, 2, 3])  # (1, 2, 3)` |

## Iteráveis e iteradores

| Função | Descrição | Exemplo |
|---|---|---|
| `all()` | `True` se todos os elementos forem verdadeiros | `all([1, 2, 3])  # True` |
| `any()` | `True` se algum elemento for verdadeiro | `any([0, 1, 0])  # True` |
| `enumerate()` | Itera retornando índice e valor | `list(enumerate(['a', 'b']))  # [(0, 'a'), (1, 'b')]` |
| `filter()` | Filtra elementos com base em uma função | `list(filter(lambda x: x > 0, [-1, 2, 0, 3]))  # [2, 3]` |
| `iter()` | Cria um iterador | `iter([1, 2, 3])` |
| `len()` | Retorna o número de itens | `len('Python')  # 6` |
| `map()` | Aplica uma função a cada item | `list(map(str.upper, ['a', 'b']))  # ['A', 'B']` |
| `max()` | Retorna o maior item | `max([4, 9, 1])  # 9` |
| `min()` | Retorna o menor item | `min([4, 9, 1])  # 1` |
| `next()` | Retorna o próximo item de um iterador | `it = iter([10, 20]); next(it)  # 10` |
| `reversed()` | Retorna um iterador reverso | `list(reversed([1, 2, 3]))  # [3, 2, 1]` |
| `range()` | Gera uma sequência de números | `list(range(1, 5))  # [1, 2, 3, 4]` |
| `sorted()` | Retorna lista ordenada | `sorted([3, 1, 2])  # [1, 2, 3]` |
| `sum()` | Soma os itens de um iterável | `sum([1, 2, 3])  # 6` |
| `zip()` | Combina iteráveis elemento a elemento | `list(zip([1, 2], ['a', 'b']))  # [(1, 'a'), (2, 'b')]` |

## Aritmética

| Função | Descrição | Exemplo |
|---|---|---|
| `divmod()` | Retorna quociente e resto da divisão | `divmod(10, 3)  # (3, 1)` |
| `pow()` | Eleva um número a uma potência | `pow(2, 3)  # 8` |
| `round()` | Arredonda um número | `round(3.14159, 2)  # 3.14` |

## Classes, objetos e atributos

| Função | Descrição | Exemplo |
|---|---|---|
| `classmethod()` | Converte método em método de classe | `@classmethod` para criar acesso sem instanciar |
| `delattr()` | Remove um atributo de um objeto | `delattr(pessoa, 'idade')` |
| `getattr()` | Retorna o valor de um atributo | `getattr(pessoa, 'nome')` |
| `hasattr()` | Verifica se um objeto tem um atributo | `hasattr(pessoa, 'nome')` |
| `isinstance()` | Verifica se é instância de uma classe | `isinstance(3, int)  # True` |
| `issubclass()` | Verifica se é subclasse | `issubclass(Aluno, Pessoa)` |
| `property()` | Cria uma propriedade gerenciada | `@property` para validar acesso a atributos |
| `setattr()` | Define o valor de um atributo | `setattr(pessoa, 'idade', 30)` |
| `staticmethod()` | Converte método em método estático | `@staticmethod` para utilitários da classe |
| `super()` | Retorna proxy para acessar métodos da classe pai | `super().__init__()` |
| `type()` | Retorna o tipo de um objeto | `type(10)  # <class 'int'>` |
| `object()` | Cria um objeto base vazio | `obj = object()` |

## Escopo e inspeção

| Função | Descrição | Exemplo |
|---|---|---|
| `callable()` | Verifica se um objeto é chamável | `callable(len)  # True` |
| `dir()` | Lista atributos e métodos de um objeto | `dir('texto')` |
| `globals()` | Retorna o namespace global | `globals()['__name__']` |
| `hash()` | Retorna o hash de um objeto | `hash('Python')` |
| `id()` | Retorna o identificador único do objeto | `id(obj)` |
| `locals()` | Retorna o namespace local | `locals()` |
| `vars()` | Retorna o `__dict__` de um objeto | `vars(pessoa)` |

## Entrada, saída e arquivos

| Função | Descrição | Exemplo |
|---|---|---|
| `input()` | Lê entrada do usuário | `nome = input('Digite seu nome: ')` |
| `open()` | Abre um arquivo | `open('dados.txt', 'r', encoding='utf-8')` |
| `print()` | Imprime valores no console | `print('Olá, mundo!')` |
| `format()` | Formata um valor | `format(1234.56, '.2f')  # '1234.56'` |

## Execução de código

| Função | Descrição | Exemplo |
|---|---|---|
| `compile()` | Compila código-fonte em objeto de código | `compile('print(2 + 2)', '<script>', 'exec')` |
| `eval()` | Avalia uma expressão Python | `eval('2 + 2')  # 4` |
| `exec()` | Executa código Python dinamicamente | `exec('x = 10; print(x)')` |
| `__import__()` | Importa um módulo programaticamente | `math = __import__('math')` |

## Diversos

| Função | Descrição | Exemplo |
|---|---|---|
| `ascii()` | Representação imprimível (somente ASCII) | `ascii('ç')  # '\xe7'` |
| `breakpoint()` | Inicia o debugger | `breakpoint()` |
| `help()` | Exibe documentação do objeto | `help(str)` |
| `hex()` | Converte inteiro para string hexadecimal | `hex(255)  # '0xff'` |
| `memoryview()` | Cria uma view de memória | `memoryview(b'ABC')` |
| `oct()` | Converte inteiro para string octal | `oct(8)  # '0o10'` |
| `repr()` | Representação "oficial" de um objeto | `repr('abc')  # "'abc'"` |
| `slice()` | Cria um objeto de fatiamento | `texto[1:5]` com `slice(1, 5)` |