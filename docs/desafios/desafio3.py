''' 
Desafio 3: classificador de desempenho

Receba o valor vendido e classifique:

menos de R$ 5.000     → BAIXO
R$ 5.000–9.999        → REGULAR
R$ 10.000–19.999      → BOM
R$ 20.000 ou mais     → EXCELENTE

Use if, elif e else.

Bônus: adicione uma meta e apresente também a porcentagem atingida. 
'''

valor_venda = float(input('Informe o valor da venda em R$: \n-> '))
meta = float(input('Informe uma meta a ser atingida em R$ \n-> '))
valor_final = (meta - valor_venda) / 100

if valor_venda < 5000 :
    print('Venda Baixa')
elif valor_venda >= 5000 and valor_venda <= 9999 :
    print('Venda Regular')
elif valor_venda > 9999 and valor_venda < 19999 :
    print('Venda Boa')
elif valor_venda >= 20000 :
    print('Venda Exelente')
else :
    print('Valor inválido')

print(f'Conforme sua venda, falta {valor_final}% para alcaçar a meta informada')