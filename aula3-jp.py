"""
Progamação Estruturada
2024.1
08/03/2024

Funções
- Encapsulamento
    - Evitar ao maximo duplicidade de codigos
- Organização do codigo
"""
def cabecalho(titulo):
    print("." * 30)
    print(titulo)
    print("." * 30)

cabecalho("Folha de pagamento")
cabecalho("Lista de fornecedores")

# Com a linha de codigo que fazem parte do def
# so vão rodar caso a palavra chave seja escrita mais embaixo.

# tabem pode aparece varias veces dependendo da quantidades de veces
# que a palavra seja escrita.

def cabecalh(titulo, largura):
    print("." * largura)
    print(titulo)
    print("." * largura)

cabecalh("Folha de pagamento", 30)
cabecalh("Lista de fornecedores", 25)

# Pode-se colocar a quantidade de pontos que existira em cada "cabecalh".

def cabeca(titulo, largura, traco="."):
    print(traco, largura)
    print(titulo)
    print(traco, largura)

cabeca("Demonstrativo de resultados", largura=30, traco="=")
cabeca("Dinhero", 30)

# Colocando a função "traco" podemos idendificar o tipo e onde colocar
# os "." ou "-" com mais facilidade.

def soma(a, b):
    return a + b

print(soma(4, 8) + soma(2, -5))

#Multiplos retornos
def subsequente(x):
    return x + 1, x + 2 # tuplas

x, y = subsequente(10)
print(x, y)

# Escopo de variaveis
print("-" * 30)

# Escopo local
def func(x):
    x = 1
    print(x)

def func2():
    x = 2 # Escopo local
    print(x)

# Escopo global
x = 0

print(x)
func(x)
func2()
print(x)

def func3():
    global x #NÃO USARRRRRRRRRRR
    x = 3
    print(x)

func3()
print(x)
print(x)
print(x)

# Todos os print abaixos do func global sera atribuidos o x do mesmo global.

def func4():
    print(x)

func4()

# E caso uma nova variavel não tenha um "x" establecido vai segui a função global.
# POREM SEMPRE SE POSSIVEL EVITAR USAR O "GLOBAL".

# exemplos

def soma(a, b):
    return a + b

def substracao(a, b):
    return a - b

def main():
    x = 10
    y = 2
    print(soma(x, y))
    print(substracao(x, y))

main()

"""
exercicios

Progamação estruturada
2024.1
08/03/2024

Funçoes - exercicios
Nota de aula 05

"""

"""
Exercicio resolvido 01
Faça uma função media(), que recebe os parametros posicionais
ap1, ap2 e ac, e retorne a média de avaliação, utilizando a formula
M = (AP1 + AP2) * 0.4 + AC * 0.2

"""

def media(ap1, ap2, ac):
    return(ap1 +ap2) * 0.4 + ac * 0,2

print(media(8, 5 ,4 ))
