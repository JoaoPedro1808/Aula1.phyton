"""
Exercicios da Ac3, Progamção estruturada
João Pedro Borges Souza Santana
2024.1

"""
#Exercicio1

def determina_tipo_triangulo(a, b, c):
  if a == b == c:
     return "Triangulo Equilátero"
  elif a == b != c or a != b == c:
     return "Triangulo Isósceles"
  elif a != b != c:
     return "Triangulo Escaleno"
  elif a + b < c:
     print("Não é um triângulo")
  
def testa_triangulo():
    print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
    print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
    print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
    print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo

testa_triangulo()

#Exercicio2

def dia_semana(dia):
     if dia == 1:
        return "Domingo"
     elif dia == 2:
        return "Segunda-feira"
     elif dia == 3:
        return "Terça-feira"
     elif dia == 4:
        return "Quarta-feira"
     elif dia == 5:
        return "Quinta-feira"
     elif dia == 6:
        return "Sexta-feira"
     elif dia ==7:
        return "Sábado"
     else:
        return "String vazia"
     
def testa_dia_semana():
    print(dia_semana(2)) # segunda-feira
    print(dia_semana(6)) # sexta-feira
    print(dia_semana(7)) # sábado
    print(dia_semana(9)) # string vazia

testa_dia_semana()

#Exercicio3

a = float(input("Informe o número: "))
b = float(input("Informe o outro número: "))
operação = float(input("Informe a operação: "))
resultado = a + b or a - b or a * b or a / b

def soma(a, b, operação):
  if operação == soma:
    return a + b
  
def substracao(a, b, operação):
  if operação == substracao:
    return a - b
  
def multiplicacao(a, b, operação):
  if operação == multiplicacao:
    return a * b
  
def divisao(a, b, operação):
  if operação == divisao:
    return a / b


   