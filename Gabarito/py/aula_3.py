# -*- coding: utf-8 -*-
"""Aula 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iarEWlvfBLL6GVU4RmL2ou3IrB-b0LEm

2.	Sabendo que a = 3, b = 7 e c = 4, informe se as expressões abaixo são verdadeiras ou falsas:
>a.	(a + c) > b<br>
>b.	b > = (a + 2)<br>
>c.	c == (b – a)<br>
>d.	(b + a) < = c<br>
>e.	(c + a) > b<br>
"""

a = 3 # 3 + 4 > 7 => False
b = 7 # 7 >= 5 => True
c = 4
print('(a + c) > b é', (a + c) > b)
print('b >= (a + 2) é', b >= (a + 2))
print('c == (b - a) é', c == (b - a))
print('(b + a) <= c é', (b + a) <= c)
print("(c + a) > b é", (c + a) > b)

"""3.	Sabendo que a = 5, b = 4, c = 3 e d = 6, informe se as expressões abaixo são verdadeiras ou falsas:
>a.	(a > c) AND (c <= d)<br>
>b.	(a + b) > 10 OR (a + b) == (c + d)<br>
>c.	(a >= c) AND (d >= c)

"""

a = 5
b = 4
c = 3
d = 6

print(a > c and c <= d)
print((a + b) > 10 or (a + b) == (c + d))
print((a >= c) and (d >= c))

"""Vamos a um caso mais real...<br>
Meta de vendas: 50.000 unidades.<br>
Usuário vai informar quantas unidades do produto foram vendidas.<br>
>1. Se a meta não for atingida, o programa deverá informar que a meta não foi atingida e ninguém recebe bonus.<br>
>2. Se a meta for atingida com menos de 500 unidades de diferença, o programa informa que a meta foi atingida e que os vendedores ganharão 5% de bonus.<br>
>3. Se a meta for ultrapassada em mais de 500 unidades, os vendedores receberão bonus de 15%. 
"""

meta = 50_000
entrada = input("Quantas unidades foram vendidas? ")
if entrada.isnumeric():
    if int(entrada) >= meta:
        if int(entrada) - meta >= 500:
            print("Bonus de 15%")
        else:
            print("Bonus de 5%")
    else:
        print("Meta não atingida")
    
else:
    print("Entrada inválida")

"""Uma loja possui 2 produtos: caixa de som e caneca.<br>
A caixa de som custa R\$ 150,00 e caneca custa R\$ 30,00. <br>
Os custos fixos da loja são de R\$ 2100.<br>
Calcule o faturamento desta loja e se obteve lucro ou prejuízo. O usuário irá informar quantas canecas e quantas caixas de som foram vendidas no período.
 
"""

# Entrada de dados
custo_fixo = 2100
qtd_caixa = input("Entre com a quantidade de caixas de som vendidas: ")
qtd_caneca = input("Entre com a quantidade de canecas vendidas: ")

# Verificação da entrada
if qtd_caixa.isnumeric() and qtd_caneca.isnumeric():
    faturamento = int(qtd_caixa) * 150 + int(qtd_caneca) * 30
    balanco = faturamento - custo_fixo

    if balanco > 0:
        print('Faturamento foi de {:+,.2f} reais e o balanco de {:+,.2f} reais'.format(faturamento, balanco))
        print("LUCRO!!!!!! TAMO RICO!!")
    elif balanco == 0:
        print('Faturamento foi de {:+,.2f} reais e o balanco de {:+,.2f} reais'.format(faturamento, balanco))
        print("Sem luco e sem prejuízo")
    else:
        print('Faturamento foi de {:+,.2f} reais e o balanco de {:+,.2f} reais'.format(faturamento, balanco))
        print("Maior prejuízo... bora sacar da nossa conta...")

else:
    print('\nDigitou alguma coisa errada. \nVerifique e digite novamente')

num = input('Entre com um número Real: ')
# print("Tipo do dado na entrada: ", type(num))

num = num.replace(",",".")
num = float(num)

print("{:,.2f}".format(num))