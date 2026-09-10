'''
Desafio 1: cadastro de funcionário

Crie variáveis para nome, idade, cargo, salário, tempo de empresa e situação do funcionário. 
Mostre algo como `Carlos | Assistente Administrativo | R$ 2.100,00 | Ativo`. 
Depois use `type()` para investigar o tipo de cada variável.

Restrição: não use listas nem dicionários ainda.
'''

nome = str(input('Digite seu nome: \n-> ')).strip()
idade = int(input('Digite sua idade: \n-> '))
cargo = str(input('Informe o seu cargo: \n-> ')).strip()
salario = float(input('Informe seu salario: \n-> '))
tempo_de_empresa = int(input('Fale quanto tempo de empresa em anos voce tem: \n-> '))
situacao = str(input('Voce está ativo ou inativo na empresa? \n')).strip()  
print(f'Voce me falou que está : {situacao}\n-> Você se chama {nome}, tem {idade} anos, seu cargo na empresa é: {cargo}, com o salario de {salario} e tem {tempo_de_empresa} anos de empresa.')
print(
	f'Tipo de cada variável armazenada:\n'
	f'nome: {type(nome)}\n'
	f'idade: {type(idade)}\n'
	f'cargo: {type(cargo)}\n'
	f'salário: {type(salario)}\n'
	f'tempo_de_empresa: {type(tempo_de_empresa)}\n'
	f'situação: {type(situacao)}'
)