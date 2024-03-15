"""
Progamação Estruturada 
2024.1
11/03/2024

Estruturadas de decisão
-if/ellif/else
-match/case
"""

def saudação (turno):
    if turno == "M":
        print("Bom dia!")
    else:
        if turno=="T":
           print("Boa trade!")
        else:
            if turno=="N":
                print("Boa noite!")
            else:
                print("Dado invalido")
    

saudação("M")
saudação("T")
saudação("N")
saudação("IUY")
print("." * 30)

# em vez disso faça isto

def saudação2(turno):
    if turno == "M":
        print("Bom dia!")
    elif turno =="T":
        print("Boa trade!")
    elif turno =="N":
        print("Boa noite!")
    else:
        print("Dado invalido!")

saudação2("M")
saudação2("T")
saudação2("N")
saudação2("IUY")
print("." * 30)

# ou tambem pode usar

def saudação3(turno):
    if turno == "M":
       return"Bom dia!"
    if turno == "T":
        return"Boa tarde"
    if turno == "N":
        return "Boa noite"
    return"Dado invalido"

saudação2("M")
saudação2("T")
saudação2("N")
saudação2("IUY")
print("." * 30)

def le_nome():
    nome = input("Informe seu nome: ")
    if not nome:
        print("Nome inválido!")

#Ternario

def e_par(num):
    if num % 2:
        return "é impar"
    return "é par"

#match/case

def saudacao(turno):
    match turno:
        case "M":
            print("Bom dia!")
        case "T":
            print("Boa tarde!")
        case "N":
            print("Boa noite!") 
        case _:
            print("Dado invalido!")

def aprovacao(conceito):
    match conceito:
        case "Bom" | "Otimo" | "Execelente":
            print("Aprovado")
        case _:
            print("Reprovado")

"""
Exercicios resolvidos 02
Implemente um progama que receba dois numeros e retorne o maior deles.

"""

def maior(a, b):
    return a if a > b else b

print(maior(10, 5))
print(maior(5, 10))

"""
Exercício resolvido 04
Faça um programa que verifique se uma letra é vogal ou consoante.
"""

def le_vogal(letra):
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print("vogal")
    else:
        print("consoate")

print(le_vogal("e"))

"""
5-Faça um programa que receba três notas, calcule sua média aritmética simples e apresente na tela uma das seguintes informações:

-A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;
-A mensagem “Reprovado”, se a média for menor do que sete;
-A mensagem “Aprovado com Distinção”, se a média for igual a dez;
-A mensagem “Nota inválida!” toda vez que for inserido um valor inválido.
"""
def nota_e_valida(nota):
    return 0 <= nota <= 10

def calcula_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if nota_e_valida(nota1) and nota_e_valida(nota2) and nota_e_valida(nota3):
        if media == 10:
            print("Aprovado com distinção")
        elif 7 <= media < 10:
            print("Aprovado")
        else:
            print("Reprovado")
    else:
        print("Nota inválida!")
        
        
        
    

