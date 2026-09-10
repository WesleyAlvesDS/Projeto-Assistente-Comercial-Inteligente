# Projeto 1: Assistente Comercial Inteligente

## Como usar este guia

Este documento organiza a evolução do projeto e a ordem recomendada de estudo. Avance por etapas e só aumente a complexidade quando o marco atual estiver funcionando.

## Índice

1. [Python](#1-python-sua-primeira-etapa)
2. [Git e GitHub](#2-git-e-github)
3. [Entendimento comercial](#3-entendimento-comercial)
4. [Modelagem de banco de dados](#4-modelagem-de-banco-de-dados)
5. [SQL](#5-sql)
6. [PostgreSQL](#6-postgresql)
7. [Excel](#7-excel)
8. [NumPy](#8-numpy)
9. [Pandas](#9-pandas)
10. [Estatística](#10-estatística)
11. [Análise exploratória](#11-análise-exploratória-eda)
12. [KPIs comerciais](#12-kpis-comerciais)
13. [Power BI](#13-power-bi)
14. [Análise multivariada](#14-análise-multivariada)
15. [Machine Learning](#15-machine-learning)
16. [API](#16-api-fastapi)
17. [Frontend](#17-frontend)

A primeira versão terá este fluxo:

Dados comerciais
      ↓
Python
      ↓
PostgreSQL / SQL
      ↓
Tratamento de dados
      ↓
Análise estatística
      ↓
KPIs comerciais
      ↓
Power BI
      ↓
Insights

### Evolução futura

             Assistente Comercial
                     │
          ┌──────────┴──────────┐
          ↓                     ↓
     Operacional              Dados
          ↓                     ↓
 Clientes/Vendas          Estatística
 Tarefas/Metas            Segmentação
 Propostas                Previsões
          │                     │
          └──────────┬──────────┘
                     ↓
                Dashboard
## 1. Python: sua primeira etapa

Você começa aqui.

Não comece por React, FastAPI, Power BI ou Machine Learning.

O que estudar
Fundamentos

Você já começou:

Variáveis e tipos
Condicionais
Loops
Funções

Listas
Tuplas
Dicionários
Sets

Strings
Entrada e saída
Arquivos
Exceções

Depois avance para:

Módulos
Pacotes
Ambiente virtual

Compreensão de listas
Funções lambda
Datas e horários
JSON
CSV

Depois:

Orientação a Objetos

Estude:

Classes
Objetos
Atributos
Métodos
Construtores
Encapsulamento
Herança
Composição

Mas não precisa virar especialista em POO antes de continuar.

Seu objetivo

Você estará pronto quando conseguir construir, sem tutorial, um programa no terminal que:

recebe dados;
valida entradas;
guarda informações;
pesquisa informações;
altera informações;
calcula resultados;
lê arquivos;
salva arquivos;
trata erros.

Esse será seu primeiro marco.

## 2. Git e GitHub

Aprenda junto com Python, não depois.

Você precisa entender:

repositório
commit
branch
merge
push
pull
.gitignore
README

Seu projeto já começa no Git.

A ideia é que o histórico mostre sua evolução:

commit: estrutura inicial
commit: cadastro de clientes
commit: validação de dados
commit: módulo de vendas
commit: relatório comercial
...

Isso é muito melhor do que terminar tudo e subir uma pasta inteira.

## 3. Entendimento comercial

Essa parte é extremamente importante.

Antes de programar o CRM completo, você precisa entender o problema.

Estude conceitos como:

Cliente
Lead
Prospect
Funil de vendas
Proposta
Conversão
Follow-up
Meta
Ticket médio
Receita
Faturamento
Margem
Churn
Carteira de clientes
Pipeline comercial
KPI

Sua formação em Dados precisa responder perguntas de negócio, não apenas gerar gráficos.

## 4. Modelagem de banco de dados

Quando sua versão Python funcionar com arquivos, avance.

Estude:

Banco relacional
Tabela
Coluna
Registro
Chave primária
Chave estrangeira
Relacionamento
Cardinalidade
Constraint
Normalização
Índice

E principalmente:

DER

Diagrama Entidade-Relacionamento.

Não copie meu modelo.

Pegue uma folha e pense:

Quais coisas existem dentro de uma operação comercial?

Você provavelmente descobrirá coisas como cliente, venda, produto etc.

Depois pergunte:

Como essas coisas se relacionam?

Esse raciocínio é justamente o exercício.

## 5. SQL

Aqui você deve investir bastante tempo.

Aprenda nesta ordem:

SELECT
WHERE
ORDER BY

INSERT
UPDATE
DELETE

GROUP BY
HAVING

INNER JOIN
LEFT JOIN
RIGHT JOIN

Subqueries
CTEs

CASE WHEN

Agregações

Window Functions

Views

Indexes

E funções de:

texto
data
matemática
agregação
Seu teste

Quando eu perguntar:

"Qual vendedor teve maior faturamento em cada mês?"

Você precisa conseguir pensar em como obter isso usando SQL.

Não decorar query.

Pensar relacionalmente.

## 6. PostgreSQL

SQL é a linguagem.

PostgreSQL será nosso SGBD.

Você vai pegar o DER que você criou e transformá-lo em banco.

A evolução será:

Python
↓
arquivos CSV/JSON

       V1

         ↓

Python
↓
PostgreSQL

       V2

Isso também vai te ensinar por que bancos de dados existem.

## 7. Excel

Não ignore Excel porque você está estudando Ciência de Dados.

Para vagas Jr de Dados e principalmente comercial/administrativo, é útil.

Estude:

Tabelas
Filtros
PROCX
ÍNDICE/CORRESP
SE
SOMASES
CONT.SES
Tratamento de texto
Datas
Tabela dinâmica
Gráficos
Power Query

Faça parte da análise comercial primeiro no Excel.

Depois compare com Python/SQL.

## 8. NumPy

Agora começa uma mudança.

Até aqui você estava construindo principalmente software e estrutura de dados.

Agora começa Ciência de Dados.

Estude:

Arrays
Dimensões
Indexação
Slicing
Vetorização
Broadcasting
Operações matemáticas
Matrizes
Álgebra linear

Mas lembre da nossa regra.

Primeiro entenda:

[10, 20, 30]

Depois entenda por que NumPy existe.

## 9. Pandas

Agora você começa a transformar o banco comercial em dataset.

Estude:

Series
DataFrame

read_csv
read_sql

head
info
describe

loc
iloc

filtros

groupby

merge
join

pivot

missing values
duplicados

apply

datas

Seu fluxo começa a ficar:

PostgreSQL
     ↓
    SQL
     ↓
   Python
     ↓
   Pandas
     ↓
Dataset analítico
## 10. Estatística

Aqui eu quero que você aproveite fortemente a faculdade.

Comece com:

População
Amostra
Variável

Qualitativa
Quantitativa

Média
Mediana
Moda

Variância
Desvio padrão

Quartis
Percentis

Distribuições
Outliers

Depois:

Probabilidade
Probabilidade condicional
Distribuição normal
Amostragem
Intervalo de confiança
Teste de hipótese
p-valor

E aqui mantenha sua filosofia de aprender "na unha".

Antes de:

dados.mean()

você deve saber o que uma média representa e como calculá-la.

## 11. Análise exploratória: EDA

Agora pegue os dados comerciais e investigue.

Não comece fazendo gráfico bonito.

Comece fazendo perguntas.

Por exemplo:

Como as vendas estão distribuídas?

Existem valores extremos?

Existem períodos fracos?

Existem diferenças entre vendedores?

Existem clientes que representam grande parte da receita?

Alguma variável parece relacionada a outra?

Você estará aprendendo a transformar:

DADOS
 ↓
PERGUNTA
 ↓
ANÁLISE
 ↓
EVIDÊNCIA
 ↓
CONCLUSÃO

Isso é muito importante para entrevista.

## 12. KPIs comerciais

Agora você precisa aprender a transformar dados em indicadores.

Estude conceitualmente:

Faturamento
Ticket médio
Conversão
Margem
Meta
Crescimento
Retenção
Churn
Recorrência
CAC
LTV

Não implemente todos só porque existem.

Pergunte:

Esse KPI faz sentido para a empresa fictícia que estou analisando?

Essa decisão também faz parte do projeto.

## 13. Power BI

Somente agora eu entraria pesado em Power BI.

Estude:

Power Query
Modelagem
Relacionamentos

Tabela fato
Tabela dimensão

Modelo estrela

DAX

Medidas
Colunas calculadas

Contexto de filtro
Contexto de linha

Depois:

KPIs
Drill-down
Filtros
Segmentadores
Tooltips
Storytelling

Seu dashboard não deve ser simplesmente:

"Olha, fiz seis gráficos."

Ele precisa responder perguntas comerciais.

## 14. Análise multivariada

Agora começamos uma versão mais avançada.

Estude na ordem:

Covariância
      ↓
Correlação
      ↓
Regressão linear
      ↓
Regressão múltipla
      ↓
ANOVA
      ↓
Padronização
      ↓
Distâncias
      ↓
Clusterização
      ↓
PCA

Não precisamos usar todos no sistema só para impressionar.

Você deve descobrir:

Existe um problema comercial em que esse método realmente seja útil?

Essa é a diferença entre projeto acadêmico e projeto profissional.

## 15. Machine Learning

Só agora.

Estude:

Aprendizado supervisionado
Aprendizado não supervisionado

Features
Target

Treino
Validação
Teste

Overfitting
Underfitting

Regressão
Classificação
Clusterização

Métricas

Depois entramos em:

Scikit-learn.

Mas alguns algoritmos serão implementados primeiro por você.

## 16. API: FastAPI

Aqui seu projeto deixa de ser apenas análise.

Estude:

HTTP
REST

GET
POST
PUT
PATCH
DELETE

JSON

Status codes

Request
Response

Endpoints

Autenticação

Depois:

FastAPI.

Arquitetura:

Frontend
    ↓
HTTP
    ↓
FastAPI
    ↓
Python
    ↓
PostgreSQL
## 17. Frontend

Por último.

Como você já tem contato com React, pode usar:

React + TypeScript.

Mas não deixe frontend roubar o foco do projeto.

A interface administrativa pode ser simples:

┌─────────────────────────────────────┐
│ Assistente Comercial                │
├──────────┬──────────────────────────┤
│ Dashboard│                          │
│ Clientes │       Conteúdo           │
│ Vendas   │                          │
│ Produtos │                          │
│ Metas    │                          │
│ Análises │                          │
└──────────┴──────────────────────────┘

O valor está nos dados, não em animações.

Sua stack final

Ao terminar, aproximadamente:

Camada	Tecnologia
Linguagem	Python
Banco	PostgreSQL
Consulta	SQL
Manipulação	Pandas
Computação	NumPy
Visualização Python	Matplotlib
Estatística	Python + posteriormente SciPy/Statsmodels
ML	Scikit-learn
BI	Power BI
Planilhas	Excel
API	FastAPI
Frontend	React + TypeScript
Versionamento	Git + GitHub
Ambiente	VS Code + Jupyter
Deploy futuro	Docker + Cloud
🗺️ Seu roteiro completo

Eu seguiria exatamente esta sequência:

01 ─ Python fundamentos
      ↓
02 ─ Git/GitHub
      ↓
03 ─ Python POO
      ↓
04 ─ Fundamentos comerciais
      ↓
05 ─ Modelagem de dados / DER
      ↓
06 ─ SQL
      ↓
07 ─ PostgreSQL
      ↓
08 ─ Excel
      ↓
09 ─ NumPy
      ↓
10 ─ Pandas
      ↓
11 ─ Estatística
      ↓
12 ─ EDA
      ↓
13 ─ KPIs
      ↓
14 ─ Power BI
      ↓
15 ─ Análise Multivariada
      ↓
16 ─ Machine Learning
      ↓
17 ─ FastAPI
      ↓
18 ─ React
      ↓
19 ─ Docker / Deploy

Mas isso não significa estudar 19 assuntos e só depois programar.

É o contrário.

Como você vai construir a V1

Seu primeiro objetivo será bem pequeno:

Construir um Assistente Comercial que funcione exclusivamente pelo terminal usando Python puro.

Ele precisa lidar conceitualmente com:

clientes → produtos → vendas → vendedores → tarefas/metas → relatórios.

Não vou definir para você quais classes, funções, estruturas ou arquivos usar. Essa decisão será seu primeiro exercício de engenharia.

Você deverá conseguir responder sozinho:

Quais dados um cliente precisa ter?

Como identificar um cliente?

Como representar uma venda?

Como relacionar venda e cliente?

Uma venda pode possuir vários produtos?

Como calcular o total?

Como impedir valores inválidos?

Como localizar um cliente?

Como persistir os dados depois que o programa fecha?

Como gerar um relatório?

E só então programar.

🎯 Seu primeiro marco

Antes de SQL, Pandas ou Power BI, sua V1 precisa funcionar com Python puro:

INICIAR
   ↓
Carregar dados
   ↓
Menu
   ├── Clientes
   ├── Vendas
   ├── Produtos
   ├── Vendedores
   ├── Tarefas/Metas
   └── Relatórios
   ↓
Processar
   ↓
Salvar
   ↓
ENCERRAR

E aqui eu faria uma mudança importante na forma como vou te ajudar daqui para frente.

Quando você trouxer código, eu posso avaliar em três níveis:

🔴 Erro: algo está conceitualmente errado.
🟡 Pista: existe uma abordagem melhor; eu indico onde pensar.
🟢 Aprovado: funciona e você pode avançar.

Sem te entregar automaticamente a solução.

Assim, o código continua sendo seu. Quando terminarmos essa V1, você terá aprendido Python através de um problema real; aí migramos os dados para SQL/PostgreSQL, e o Assistente Comercial começa a se transformar efetivamente em um projeto profissional de Dados.

## Como começar

Eu começaria sem programar o Assistente Comercial inteiro. Seu primeiro objetivo é criar uma versão mínima que force você a usar os fundamentos de Python que está estudando.

Etapa 1 — Defina o problema no papel

Imagine uma pequena empresa com alguns vendedores. Ela atualmente controla tudo em planilhas e quer organizar clientes e vendas.

Sua V0.1 terá apenas três responsabilidades:

ASSISTENTE COMERCIAL
        │
        ├── Clientes
        │
        ├── Vendas
        │
        └── Relatório

Nada de banco, Pandas, interface, API ou Power BI ainda.

Sua primeira missão é pensar em quais dados são necessários. Não vou definir os campos por você. Pergunte-se: "O que preciso saber sobre um cliente para identificá-lo e contatá-lo?" e "O que preciso registrar para saber quem comprou, quanto comprou, quando e com quem?". Escreva suas decisões em um README.md.

Etapa 2 — Prepare seu projeto

Crie um repositório no GitHub chamado, por exemplo:

assistente-comercial

Localmente, comece simples:

assistente-comercial/
│
├── README.md
├── main.py
└── .gitignore

Não crie 30 arquivos agora. Conforme você sentir que main.py está ficando grande demais, isso vai criar uma oportunidade para estudar módulos e organização de código.

Seu primeiro commit pode representar apenas a inicialização do projeto.

Etapa 3 — Seu primeiro desafio de programação

Agora abra main.py.

Quero que você consiga produzir sozinho algo conceitualmente equivalente a:

=============================
    ASSISTENTE COMERCIAL
=============================

1 - Clientes
2 - Registrar venda
3 - Relatório
0 - Sair

Escolha uma opção:

Não copie código meu porque propositalmente não estou fornecendo.

Para conseguir fazer isso, revise somente:

print() → input() → variáveis → tipos → if/elif/else → while.

Sua primeira tarefa é fazer o menu permanecer funcionando até o usuário escolher Sair.

Critérios de conclusão

Teste:

Escolha: 1
→ alguma resposta relacionada a clientes

Escolha: 2
→ alguma resposta relacionada a vendas

Escolha: 3
→ alguma resposta relacionada ao relatório

Escolha: 99
→ opção inválida

Escolha: 0
→ programa encerrado

Não avance enquanto isso não estiver funcionando.

Etapa 4 — Clientes

Agora seu primeiro problema real.

Você precisa permitir:

CLIENTES

1 - Cadastrar
2 - Listar
3 - Buscar
4 - Alterar
5 - Voltar

Para conseguir fazer isso, você terá que estudar:

listas + dicionários + loops + funções + strings.

E aqui começam as decisões que eu quero que você tome.

Como armazenar vários clientes?

Como garantir que cada cliente tenha uma identificação?

Como procurar determinado cliente?

Como saber se ele já existe?

Como alterar somente um dado?

Como impedir um cadastro vazio?

Não procure "código de CRM Python". Procure os conceitos necessários para resolver cada problema.

Etapa 5 — Vendas

Somente quando Clientes funcionar.

Agora seu sistema precisa registrar uma venda relacionada a um cliente.

Você terá que descobrir como representar algo conceitualmente assim:

CLIENTE
   │
   └── possui
         │
       VENDAS

Seu programa deverá conseguir responder perguntas como:

Quem realizou a compra?

Qual foi o valor?

Quando aconteceu?

Quem vendeu?

Novamente, os campos exatos são decisão sua.

Aqui você vai praticar principalmente estruturas de dados, funções, validações, loops e relacionamento entre informações.

Etapa 6 — Seu primeiro módulo de Dados

Agora começa a aparecer seu perfil de Ciência de Dados.

Com várias vendas registradas, crie a opção:

RELATÓRIO COMERCIAL

Ela deve responder pelo menos a perguntas como:

Quanto a empresa vendeu?

Quantas vendas ocorreram?

Qual foi o valor médio?

Qual foi a maior venda?

Qual foi a menor?

Qual cliente mais comprou?

Qual vendedor mais vendeu?
Regra importante

Na primeira implementação, tente construir os cálculos manualmente.

Se precisar calcular uma média, pense no algoritmo:

Tenho vários valores
        ↓
Como percorro esses valores?
        ↓
Como acumulo?
        ↓
Como descubro quantos existem?
        ↓
Como obtenho a média?

É exatamente esse raciocínio que posteriormente permitirá entender Pandas, estatística e algoritmos.

Etapa 7 — Faça o sistema sobreviver

Até aqui você encontrará um problema:

"Fechei o programa e perdi todos os clientes."

Ótimo. O próprio projeto acabou de criar seu próximo assunto de estudo.

Agora estude:

arquivos → with open() → leitura/escrita → CSV → JSON → exceções.

Faça o programa chegar ao comportamento:

ABRIR PROGRAMA
      ↓
Carregar dados existentes
      ↓
Trabalhar
      ↓
Cadastrar / alterar
      ↓
Salvar
      ↓
FECHAR

        ↓ amanhã ↓

ABRIR
      ↓
Dados continuam lá

Quando conseguir isso, considero sua V0.1 concluída.

O que você NÃO deve estudar agora

Esse ponto é importante para não se perder.

Neste momento, deixe de lado:

Pandas, NumPy, PostgreSQL, Power BI, FastAPI, React, Scikit-learn, Machine Learning, PLN e Docker.

Eles virão.

Seu universo agora é somente:

Python
│
├── variáveis/tipos
├── condicionais
├── loops
├── funções
├── listas
├── dicionários
├── sets/tuplas
├── strings
├── exceções
└── arquivos

+

Git/GitHub
Seu primeiro ciclo de estudo

Não faça:

"Vou terminar um curso de 40 horas de Python e depois começar."

Faça:

ESTUDAR
  ↓
30–60 minutos
  ↓
TENTAR NO PROJETO
  ↓
ERRO
  ↓
PESQUISAR O CONCEITO
  ↓
TENTAR NOVAMENTE
  ↓
FUNCIONOU
  ↓
COMMIT
  ↓
PRÓXIMO PROBLEMA
Portanto, sua tarefa de hoje é pequena

1. Crie a pasta/repositório assistente-comercial.

2. Crie README.md, .gitignore e main.py.

3. No README, escreva com suas próprias palavras qual problema seu Assistente Comercial pretende resolver.

4. Defina as três primeiras áreas: Clientes, Vendas e Relatórios.

5. Faça somente o menu principal funcionar em loop, incluindo tratamento de opção inválida e saída.

Pare aí.

Quando fizer isso, pode me mandar o seu main.py, mesmo que esteja ruim. Eu vou revisar como professor: aponto o que está correto, o que precisa melhorar e dou pistas — sem entregar o gabarito. A partir daí, passamos para Cadastro de Clientes.