"""
Progamção Estruturada
2024.1
18/03/2024

Estrutura de repetição
- while -> quando não sabemos quantas veces vamos executar a repetição.

- for -> quando queremos acessar todos os elemento de uma coleção de dados.

"""
"""
def contagem_regressiva(num):
    while num >= 0:
        print(num) #loop infinito

contagem_regressiva(5)
"""

def contagem_regressiva(num):
    while num >= 0:
        print(num) 
        num -= 1 #num = num - 1

    print("acabou")

contagem_regressiva(5)

print("." * 30)

# range ({start}, stop, {step})
#start - inclusive
#stop - exclusive 
#step - passo

print(list(range(5)))         #0, 1, 2, 3, 4
print(list(range(2, 5)))      #2, 3, 4
print(list(range(2, 10, 3)))  #2, 5, 8
print(list(range(10, -5, 2))) #nada

def contagem_regressiva2(num):
    for cont in range(num, -1, -1): #5, 4, 3, 2, 1, 0
        print(cont)

contagem_regressiva2(5)

print("." * 30)

def ola_varias_veces(n):
    #cracteristicas curinga 
    for cont in range(n):
        print("olá")

ola_varias_veces(5)

def pula_mult_3(maximo):
    for x in range(1, maximo + 1):
        if x % 3 ==0:
            continue #pula para a proxima interação
        print(x)

pula_mult_3(10)

def para_antes_de_10(maximo):
    for x in range(1, maximo + 1):
        if x >= 10:
            break #interrompe por completo a estrutura rep
        print(x)

print("acabou")

print("." * 30)
para_antes_de_10(20)


def e_primo(num):
    for div in range(2, num):
        if num % div == 0:
            print(num, "não é primo")
            break
    else:
        print(num, "é primo")

e_primo(7)
e_primo(11)
e_primo(2)
e_primo(35)

"""
Exercecicios nota de aula 07
elabora uma função conta_pares(min, max) para exibir todos os valores
entre min e max, inclusive, com um incremento de 2, separando-os com um
hiffen, ex: 2 - 4 - 6 - 8 - 10 - 12 - 14.
"""

def conta_pares(min, max):
    for n in range(min, max + 1):
        if n % 2 == 0:
          if n >= max -1:
           print(n)
          else:
           print(n, end= "-")



conta_pares(2, 14)
conta_pares(1, 9)
conta_pares(1, 8)
conta_pares(2, 9)

"""
Faça um progama que calcule o fatorial de um número inteiro
positivo fornecido pelo usuario.
Ex: 5! = 5 * 4 * 3 * 2 * 1 = 120
"""

def fatorial(num):
    if num == 1:
        return 1
    return num * fatorial(num - 1)

print(fatorial(5))




       


