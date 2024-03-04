"""
Progmação Estruturada
2024.1
04/03/2024

Operadores
- Aritimeticos
- Atribuição
- Comparação (ou relacionais)
- Logicos (ou booleanos)
"""

# Operadores arimeticos.
# Quando os operadores são numericos.
x = 7.2
y = 8.4

print(x + y)   # Soma
print(x - y)   # Substração
print(x * y)   # Multiplicação
print(x / y)   # Divisão
print(x ** y)  # Potencia
print(x // y)  # Divisão inteira
print(x % y)   # Modulo

print(round(x + y, 2))

# O roundo redondeia o resultado com o 2 no final especificando
# a quantidad de decimais maxime que o resultado deve cubrir
# Em vez de ficar tipo 15.600000000000001 fica no final 15.6.

#Quando pelo menos um operando é str:
print("Hello,"+ " world") # Concatenação de string     str + str
print("-" * 30)          # Multiplicação de string    str + int

# A multiplicação de string multiplica o que esta dentro da ()
# com a quantidade de vezes colacada ao lado.

# Operadores de atribuição
x = 10
x += 2 # x = x + 2
x -= 1 # x = x - 1
x *= 2 # x = x * 2
print(x)

# operdaores de comparção ou relacionais.
# Retornam um booleano (True / False).
x = 10
y = 3

print("-" * 30)
print(x > y)   # maior a...
print(x >= y)  # maior ou igual a...
print(x < y)   # menor a...
print(x <= y)  # menor ou igual a...
print(x == y)  # igual a
print(x != y)  # diferente a

print("-" * 30)

# Tambem funciona com letras com o fator que determina qual e o maior
# sendo a quantidade a maiusculas na frase ou no conjunto.

x = "abc"
y = "aBc"

print(x > y)   # maior a...
print(x >= y)  # maior ou igual a...
print(x < y)   # menor a...
print(x <= y)  # menor ou igual a...
print(x == y)  # igual a
print(x != y)  # diferente a

# Operadores logicos
print("-" * 30)
print(True and False) # E, tem que ter todos (V) para ser (V) e tem ter um (F) para ser (F).
print(True or False)  #OU, tem ter todos (F) para ser (F) e tem ter um (V) para ser (V).
print(not True)       #NÃO, inverte os valores logicos.

print("-" * 30)
print(int(6.0))        #Converte para int.
print(float("10.42"))  #Converte para float.
print(bool("10"))      #Converte para bool.

#qualquer coisa diferente de 0, 0.0, "", {}, [], () como true
#Problemna do "and"
print("-" * 30)
print("a" and 16)  #Caso o primero for (V) vai voltar para o ultimo.
print(0 and "abc") #Caso o primero for (F) não vai ler o ultimo.

print("" and int("b"))

print("a" or 16)     #16
print(0.0 or "abc")  #0.0

print(0.0 or "")        #""
print(1.5 and "texto")  #texto

"""
Operação and
-Se o primeiro operando é true, retorna o segundo operando.
-Se o primeiro operando é false, retorna o primeiro operando.

Operação or
-Se o primeiro operando é false, retorna o segundo operando.
-Se o primeiro operando é true, retorna o primeiro operando.
"""

"""

Precendencia
()
**
* / // %
+ -
> >= < <= == !=
not x
and
or
=

"""
print("-" * 30)
print(4 + 6 / 2 **2 > 10 // 3 and 4.5 - 2 or not 10 % 3 <= 2)
print(4 + 6 / 4 > 10 // 3 and 4.5 - 2 or not 10 % 3 <= 2)
print(4 + 6 / 4 > 3 and 4.5 - 2 or not 1 <= 2)
print(4 + 1.5 > 3 and 4.5 - 2 or not 1 <= 2)
print(5.5 > 3 and 2.5 or not 1 <= 2)
print(True and 2.5 or not True)
print(True and 2.5 or False)
print(2.5)

"""
Nota de aula 4
Exercicio resolvido 01
Faça um programa que peça as tres notas (AP1, AP2 E AC) e mostre a media.
A media e calculada de acordo com a formula
M = (AP1 + AP2) * 0.4 + AC * 0.2.
"""
ap1 = float(input("Informe a sua nota da AP1: "))
ap2 = float(input("Informe a sua nota da AP2: "))
AC = float(input("Informe a sua nota da AC: "))
Media = (ap1 + ap2) * 0.4 + AC * 0.2
print("A sua media é ", Media)

