# Lista de desafios: fundamentos de Python

A dificuldade vai aumentando progressivamente. Os primeiros treinam um conceito isolado; no final, você vai juntar praticamente tudo.

## Visão geral

| # | Desafio | Conceitos | Nível |
|---:|---|---|:---:|
| 1 | Cadastro de funcionário | Variáveis e tipos | 🟢 |
| 2 | Calculadora de comissão | Variáveis e operações | 🟢 |
| 3 | Classificador de vendas | Condicionais | 🟢 |
| 4 | Analisador de metas | Loops | 🟢 |
| 5 | Calculadora comercial | Funções | 🟡 |
| 6 | Analisador de vendas | Listas | 🟡 |
| 7 | Ranking sem `sort()` | Listas e loops | 🟡 |
| 8 | Cadastro de clientes | Dicionários | 🟡 |
| 9 | Identificador de clientes únicos | Sets | 🟡 |
| 10 | Sistema resistente a erros | Exceções | 🟡 |
| 11 | Relatório comercial | Arquivos | 🟡 |
| 12 | Mini CRM | Todos os fundamentos | 🔴 |

## Desafios 1 a 4: lógica básica

### Desafio 1: cadastro de funcionário

Crie variáveis para nome, idade, cargo, salário, tempo de empresa e situação do funcionário. Mostre algo como `Carlos | Assistente Administrativo | R$ 2.100,00 | Ativo`. Depois use `type()` para investigar o tipo de cada variável.

Restrição: não use listas nem dicionários ainda.

### Desafio 2: calculadora de comissão

Um vendedor vendeu R$ 18.500 no mês e recebe 4% de comissão. Calcule a comissão e o salário final, considerando salário-base de R$ 1.800.

Depois faça o programa receber os valores pelo teclado usando input().

Bônus: descubra sozinho por que isto dá problema:

vendas = input("Vendas: ")
comissao = vendas * 0.04

### Desafio 3: classificador de desempenho

Receba o valor vendido e classifique:

menos de R$ 5.000     → BAIXO
R$ 5.000–9.999        → REGULAR
R$ 10.000–19.999      → BOM
R$ 20.000 ou mais     → EXCELENTE

Use if, elif e else.

Bônus: adicione uma meta e apresente também a porcentagem atingida.

### Desafio 4: analisador de metas

Considere:

vendas = [7200, 8500, 4900, 12000, 15700, 6300]

Sem usar sum(), max() ou min(), descubra:

Total vendido
Maior venda
Menor venda
Quantidade de vendas
Quantidade acima de R$ 10.000

Aqui você começa a aprender a pensar como um algoritmo.

## Desafios 5 a 7: funções e estruturas

### Desafio 5: calculadora comercial

Transforme os cálculos anteriores em funções.

Você deve criar, por exemplo:

calcular_comissao()
calcular_total()
calcular_media()
verificar_meta()
classificar_desempenho()

Não estou te dando a implementação, somente a responsabilidade de cada função.

O programa principal deve chamá-las.

### Desafio 6: análise estatística inicial

Use:

vendas = [
    1250.50,
    890.00,
    2100.00,
    750.90,
    3200.00,
    1750.00,
    4100.00
]

Implemente você mesmo, sem statistics, NumPy ou Pandas:

número de observações
soma
média
mínimo
máximo
amplitude
⭐ Bônus importante

Implemente também:

mediana
variância
desvio padrão

Esse desafio começa a conectar Python → Estatística → Ciência de Dados.

### Desafio 7: ranking de vendedores

Dados:

vendedores = [
    ["Ana", 12500],
    ["Carlos", 8700],
    ["Bruno", 19200],
    ["Maria", 14300],
    ["Pedro", 6800]
]

Produza:

1º Bruno  - R$ 19.200
2º Maria  - R$ 14.300
3º Ana    - R$ 12.500
...
Regra especial

❌ Não pode usar:

sorted()
.sort()

Você terá que descobrir como ordenar os valores manualmente.

Esse é excelente para lógica de programação.

## Desafios 8 a 10: dados estruturados

### Desafio 8: cadastro de clientes

Represente clientes usando dicionários:

cliente = {
    "id": 1,
    "nome": "Mercado Central",
    "cidade": "Nova Friburgo",
    "compras": 8,
    "valor_total": 12450.00,
    "ativo": True
}

Crie pelo menos 5 clientes.

Seu programa deverá descobrir:

Quantidade de clientes
Clientes ativos
Clientes inativos
Cliente que mais gastou
Valor médio por cliente
Clientes com compras > R$ 5.000

Não use Pandas.

### Desafio 9: clientes únicos

Imagine que uma lista de IDs de clientes possui duplicações:

clientes = [
    101, 102, 103, 101,
    104, 102, 105, 106,
    103, 107
]

Descubra:

quantos registros existem
quantos clientes diferentes existem
quais IDs aparecem duplicados

Aqui você deve explorar set.

Bônus difícil: descubra quantas vezes cada cliente aparece.

### Desafio 10: entrada de dados resistente a erros

Faça um programa perguntar:

Nome:
Valor da venda:
Quantidade:

O usuário poderá fazer coisas erradas:

Valor da venda: banana
Quantidade: dez
Valor da venda: -300
Nome:

Seu programa não deve simplesmente quebrar.

Use:

try
except
else
finally

E validações próprias.

## Desafio 11: arquivos

Agora começamos a simular uma empresa de verdade.

Crie:

vendas.csv

Com algo como:

id,cliente,vendedor,valor
1,Mercado Central,Ana,1250.50
2,Loja Silva,Carlos,890.00
3,Empresa XPTO,Ana,2100.00
4,Loja Brasil,Maria,750.90
5,Mercado Central,Ana,3200.00

Mas existe uma condição:

❌ Pandas proibido.

Leia o arquivo usando Python.

Seu programa deverá descobrir:

Faturamento total
Número de vendas
Ticket médio
Maior venda
Menor venda
Vendas por vendedor
Faturamento por vendedor
Número de clientes únicos
Melhor vendedor

Depois crie automaticamente:

relatorio.txt

contendo os resultados.

Esse já é um mini projeto de análise de dados.

## Desafio 12: mini CRM

Esse é o seu "chefão" dos fundamentos.

Crie um programa no terminal:

================================
      ASSISTENTE COMERCIAL
================================

[1] Cadastrar cliente
[2] Listar clientes
[3] Registrar venda
[4] Listar vendas
[5] Buscar cliente
[6] Estatísticas
[7] Exportar relatório
[0] Sair

Escolha:

Você deverá trabalhar com:

clientes
vendas

Cada cliente pode ter:

ID
Nome
Telefone
Cidade
E-mail
Status

Cada venda:

ID
Cliente
Valor
Data
Vendedor

O módulo Estatísticas deverá apresentar:

Faturamento
Número de vendas
Ticket médio

Maior venda
Menor venda

Clientes ativos
Clientes únicos

Melhor vendedor
Melhor cliente

E os dados precisam sobreviver quando o programa fechar.

Portanto:

Programa inicia
      ↓
lê arquivos
      ↓
carrega dados
      ↓
usuário trabalha
      ↓
altera dados
      ↓
salva arquivos
      ↓
programa fecha
🚫 Regras do Mini CRM

Aqui está a parte que fará você aprender:

Você pode usar:

Python puro
listas
dicionários
sets
tuplas
funções
loops
arquivos
exceções

Você ainda NÃO pode usar:

❌ Pandas
❌ NumPy
❌ SQL
❌ PostgreSQL
❌ Scikit-learn
❌ FastAPI
❌ Django

Porque essas ferramentas esconderiam justamente aquilo que estamos tentando aprender.

🎯 Sua sequência

Eu não faria os 12 de qualquer jeito. Faça:

1 → 2 → 3 → 4 → 5 → 6

Quando chegar no 6, vale parar um pouco. É nele que seus fundamentos de programação começam a se encontrar com estatística.

Depois:

7 → 8 → 9 → 10 → 11

E finalmente:

12 — Mini CRM.

Quando o Mini CRM estiver funcionando, você estará pronto para a próxima etapa do projeto:

Python puro
    ↓
Orientação a Objetos
    ↓
SQL
    ↓
PostgreSQL
    ↓
Pandas / NumPy
    ↓
Estatística
    ↓
Análise Multivariada
    ↓
PLN
    ↓
Machine Learning

E tem uma regra que eu gostaria que você adotasse durante essa trilha: quando travar, não me peça imediatamente a solução. Mande seu código e diga "me dê uma pista sem resolver". Eu posso apontar onde está o problema e qual conceito revisar, mantendo a implementação com você. Isso vai ser muito mais valioso para o objetivo que você definiu de aprender a programar e implementar algoritmos por conta própria.