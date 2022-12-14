# -*- coding: utf-8 -*-
"""Cópia de Aula_2_2022.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SLmK7zJZDvRZzOc6NZ3fLXitAaF1QSGG

#SEGUNDA AULA DE PYTHON

##1 - Operadores Lógicos
Diferente dos operadores aritméticos, os operadores lógicos retornam **True** 😀 ou **False** 😠 como resposta.

###Operadores Relacionais
São aqueles que fazem a comparação entre dois ou mais valores.

####1. Operador de igualdade (==)
"""

# Colocar 7 == 7, verificar a resposta na execussão do programa;

# Colocar 7 == 5, verificar a resposta na execussão do programa;

"""####2. Operadores menor que (<) e maior que (>)

"""

# Colocar 7 < 7, verificar a resposta na execussão do programa;

# Colocar 7 < 10, verificar a resposta na execussão do programa;

# Colocar 7 > 7, verificar a resposta na execussão do programa;

# Colocar 7 > 5, verificar a resposta na execussão do programa;

"""####3. Operadores menor ou igual que (<) e maior ou igual que (>)"""

# Colocar 7 <= 7, verificar a resposta na execussão do programa;

# Colocar 7 <= 10, verificar a resposta na execussão do programa;

# Colocar 7 >= 7, verificar a resposta na execussão do programa;

# Colocar 7 >= 5, verificar a resposta na execussão do programa;

"""####4. Operador de diferente (!=)"""

# Colocar 7 != 7, verificar a resposta na execussão do programa;

# Colocar 7 != 5, verificar a resposta na execussão do programa;

"""##2 - Tabelas Verdade
São tabelas que mostram algumas situações de entrada e suas saídas

####1. Tabela do E (AND)
O operador **AND** deve ser usado quando temos 2 ou mais condições que devem ser verdadeiras para o programa executar a ação desejada
"""

print("|   A\t|   B\t| SAÍDA |")
print("|",False,"|",False,"|",False and False,"|")
print("|",True,"\t|",False,"|",True and False,"|")
print("|",False,"|",True,"\t|",False and True,"|")
print("|",True,"\t|",True,"\t|",True and True,"\t|")

# EXEMPLO: Verificar se uma idade é maior do que a 17 E menor do que 71.

idade = int(input("Idade: "))
print(idade > 17 and idade < 71)

"""####2. Tabela do OU (OR)
O operador **OR** deve ser usado quando, pelo menos, 1 das condições for verdadeira para realizar uma ação desejada
"""

print("|   A\t|   B\t| SAÍDA |")
print("|",False,"|",False,"|",False or False,"|")
print("|",True,"\t|",False,"|",True or False," |")
print("|",False,"|",True,"\t|",False or True," |")
print("|",True,"\t|",True,"\t|",True or True," |")

# EXEMPLO: Verificar se uma idade é menor do que a 18 OU maior do que 70.

idade = int(input("Idade: "))
print(idade < 18 or idade > 70)

"""####3. Tabela do XOR (^)"""

print("|   A\t|   B\t| SAÍDA |")
print("|",False,"|",False,"|",False ^ False,"|")
print("|",True,"\t|",False,"|",True ^ False,"\t|")
print("|",False,"|",True,"\t|",False ^ True,"\t|")
print("|",True,"\t|",True,"\t|",True ^ True,"|")

# Reprodução de porcos
# Coloque 0 para leitão e 1 para leitoa em uma lista

"""####4. Tabela de Negação (not)"""

print("|   A\t| Não A |")
print("|",False,"|",not False,"\t|")
print("|",True,"\t|",not True,"|")

"""##3 - Condicionais

#### Condição SE (IF)
Usamos este tipo de condicional quando necessitamos que o programa teste algumas condições. Caso a condição seja verdadeira, o programa executará uma ação destinada àquela condição.

```
if condição 1:
    bloco de códigos do if

```
Faz-se necessário que o código tenha esta estrutura, senão o Python apresentará erro de identação.
"""

n = 3
if n == 2:
    print("{} igual a 2".format(n))

"""#### Condição SENÃO (ELSE)
Para usar o else, temos que ter usado o if antes.
```
if condição 1:
    bloco de códigos do if
    
else:
    bloco de código do else.
    Aqui finaliza a condicional
```
"""

n = 3
if n == 2:
    print("{} igual a 2".format(n))
else:
    print("{} diferente a 2".format(n))

"""#### Condição SENÃO SE (ELIF)
O elif deve ser utilizado quando temos mais do que uma condição.


```
if condição 1:
    bloco de códigos do if

elif condição 2:
    bloco de código do elif
    
else:
    bloco de código do else.
    Aqui finaliza a condicional
```


"""



"""##4 - Exercícios

###1 - Qual o maior.
*Escreva um programa que recebe 2 valores e devolve o maior entre eles.*
"""

# Declaração da variável 1

# Declaração da variável 2

# Imprimir na tela mensagem: "O X é maior do que o Y"

"""### 2 - Calculadora de preço da laranja.
*Cada laranja custa R\$ 0,3. Mas quando compradas acima de uma dúzia, seu valor cai para R\$ 0,25 cada*
"""

# Declarar a entrada da quantidade de laranjas a ser comprada

# Declaração de if

# Declaração else

# Imprimir na tela a mensagem: "x laranjas por Y reais totaliza: R$ Z"

"""###3 - Caluladora de Peso Ideal 
Fazer uma calculadora em que o usuário digita Altura em metros e Peso em quilos e se é do sexo biológico Masculino ou Feminino. O programa devolve ao usuário a informação qual seu peso ideal e quando precisa emagrecer para chegar lá. 
Ao final, o programa deve trazer uma frase motivadora para aqueles que estão acima do peso, frase parabenizando os que estão no peso ideal e uma outra frase de alerta aos que estão abaixo do peso.
***Fórmulas***

        >Masculino: (72.7 * Altura) - 50
        >Feminino: (62.1 * Altura) - 44.7

"""

# Declarar a entrada da Altura

# Declarar a entrada do Peso

# Declarar a entrada do Sexo Biológico

# Declaração de if para calcular peso ideal

# Declaração de elif para calcular peso ideal

# Declaração else

# Calcular diferença entre peso ideal e peso atual

# Declaração de if para acima do peso - A devolutiva para o usuário vem dentro do if

# Declaração de elif para abaixo do peso - A devolutiva para o usuário vem dentro do elif

# Declaração de else - A devolutiva para o usuário vem dentro do else

"""###4 - É triangulo ou Não é triângulo?
Para determinar se 3 segmentos de reta formam um triângulo, podemos fazer a verificação se a soma dos dois menores segmentos é maior do que o segmento maior.

---
    Segmentos: 2, 3 e 4
    Soma dos dois menores: 2 + 3 = 5
    Verificação: 5 > 4
    Conclusão:Estes segmentos formam um triângulo
---
"""

# Declaração do primeiro segmento

# Declaração do segundo segmento

# Declaração do terceiro segmento

# Neste if, usar AND para avaliaar se o 1º segmento é o menor

# Neste elif, usar AND para avaliaar se o 2º segmento é o maior

# Neste elif, usar AND para avaliar se o 3º segmento é o maior

# Else para possíveis erros de digitação

# Verificação se é triângulo e informar ao usuário.

"""##Desafio
Um posto de gasolina está vendendo combustíveis com a seguinte tabela de descontos:
**Gasolina:**
>Até 20 litros: desconto de 4% por litro<br>
>Acima de 20 litros: desconto de 6% por litro<br>

**Álcool:**
>Até 20 litros: desconto de 3% por litro<br>
>Acima de 20 litros: desconto de 5% por litro<br>

Escreva um programa que leia o tipo de combustível (A - Álcool e G - Gasolina), calcule e imprima o valor a ser pago pelo cliente.

---

*PARA TORNAR O DESAFIO INTERESSANTE, VAMOS FAZER O PROGRAMA CRIAR UM NÚMERO ALEATÓRIO PARA O ABASTECIMENTO. ESTE NÚMERO DEVERÁ SER ENTRE 1 E 52*

---
"""

