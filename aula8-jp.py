"""
Progamção Estruturada
2024.1
15/04/2024

Biblioteca, Pacotes, e a Biblioteca padrão do phyton

- Módulo: Arquivo phyton
- Pacote: Conjuntos de módulos
- Biblioteca: Conjuntos de pacotes
"""

import random as rnd          #<-------  Random e substituido por rnd.

print(rnd.randint(1, 10))

from random import randint      #<------ Em ves de colocar o random.randint coloca direto o randint.

print(randint(1, 10))

# Atalho

from random import randint as rint  #<----- Um apellido para randint fazendo a mesma função.

print(rint(1, 10))

from pprint import pprint

dicio = {
    "Aluno:" "João Pedro"
    "Nascimento:" "18/08/2005"
    "CPF:" "097.788.681-66"
}

pprint(dicio, indent=4)

lista = [4, 6, 2, 1, 10]
nova_lista = sorted(lista)
print(lista)
print(nova_lista)

import time

inicio = time.time()
print(time.time())

