"""
Programação Estruturada
2024.1
15/03/2024

Estruturas de Decisão
AC4
"""

def ler_nome():
    return input("Informe o nome do aluno: ")

def ler_notas():
    ap1 = float(input("Informe a sua nota da AP1: "))
    ap2 = float(input("Informe a sua nota da AP2: "))
    asub = float(input("Informe a sua nota da AS: "))
    ac = float(input("Informe a sua nota da AC: "))
    return ap1, ap2, asub, ac

def notas_sao_validas(ap1, ap2, asub, ac):
    return 0 < ap1 <= 10 and 0 < ap2 <= 10 and 0 < asub <= 10 and 0 < ac <= 10

def selecionar_notas(ap1, ap2, asub):
    if asub > ap1 and asub < ap2:
        return asub, ap2
    elif asub < ap1 and asub > ap2:
        return ap1, asub
    else:
        return ap1, ap2

def calcular_media(nota1, nota2, ac):
    return (nota1 + nota2) * 0.4 + 0.2 * ac

def aluno_foi_aprovado(media):
    return media >= 7

def analisar_media(media):
    print(media)
    if aluno_foi_aprovado(media):
        print("Aluno foi aprovado.")
    else:
        print("Aluno foi reprovado.")

def main():
    nome = ler_nome()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if notas_sao_validas(ap1, ap2, asub, ac):
            nota1, nota2 = selecionar_notas(ap1, ap2, asub)
            media = calcular_media(nota1, nota2, ac)
            analisar_media(media)

main()