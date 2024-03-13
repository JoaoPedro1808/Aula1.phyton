"""
Exercicios da Ac2, Progmação estruturada
João Pedro Borges Souza santana
2024.1

"""

#Exercicio 1,1

def eq_seg_grau(a, b, c):
    delta1 = b**2 - 4 * a * c
    return (-b + delta1 ** 0.5) / (2 * a), (-b - delta1 ** 0.5) / (2 * a) 

def main():
    x = 1
    y = -6
    z = 8
    print(eq_seg_grau(x, y, z))
   
main()
    
#Exercicio 1,2

def bisexto(ano):
    return ano%4 ==0 and ano%100 !=0 or ano%400 ==0

def main():
    ano = 2000
    print(bisexto(ano))

main()

#Execicio 2

def calcula_salario(valor_hora, num_horas, irpf=0.275):
    salario = valor_hora * num_horas 
    salario_com_irpf = salario * irpf
    return salario - salario_com_irpf

def main():
    x = 150
    y = 120
    print(calcula_salario(x, y))

main()












    
