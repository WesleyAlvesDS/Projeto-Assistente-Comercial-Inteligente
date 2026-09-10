'''
### Desafio 2: calculadora de comissão

Um vendedor vendeu R$ 18.500 no mês e recebe 4% de comissão. 
Calcule a comissão e o salário final, considerando salário-base de R$ 1.800.

Depois faça o programa receber os valores pelo teclado usando input().

Bônus: descubra sozinho por que isto dá problema:

vendas = input("Vendas: ")
comissao = vendas * 0.04

'''
COMISSAO = 4/100 
valor_venda = float(input('Digite o valor da venda mensal: \n-> '))
salario_base = float(input('Informe o salario-base: \n-> '))
salario_final = (valor_venda * COMISSAO) + salario_base
r_bonus = 'De certa forma não existe erro, o problema é no entendimento da variavel, ' \
'pois, a variavel a variavel vendas , segundo que irá prencher poderá colocar mais de um valor e isso quebra o sistema, ' \
'alem que na variavel comissao , está armazenando um calculo, sendo que em teoria ela deveria ser uma CONSTANTE'

print(f'De acordo com 4% de comissão sobre a venda total mensal, seu salario total vai ser de: {salario_final} R$')
print(f'R do Bonus: ')