"""
Exercicios da Ac5, Progmação estruturada
João Pedro Borges Souza santana
2024.1
"""

import random

def main():
    av_vida = 100
    av_atk = random.randint(10, 20)
    av_def = random.randint(1, 5)

    mons_vida = random.randint(60, 80)
    mons_atk = random.randint(20, 30)

    print(f"Aventureiro: Vida {av_vida} - Atk  {av_atk} - Def {av_def}")
    print(f"Monstro: Vida {mons_vida} - Atk {mons_atk}")

    num_rodada = 1
    while av_vida > 0 and mons_vida > 0:
        print(f"Rodada {num_rodada}")
        print("-" * 30)
        
        av_dano = random.randint(1, av_atk)
        mons_vida -= av_dano
        if mons_vida <= 0:
            print("O monstro morreu!")
            break
        
        mons_dano = random.randint(1, mons_atk) - av_def
        av_vida -= mons_dano
        if av_vida <= 0:
            print("Você morreu!")
            break
        
        print(f"Aventureiro: Vida {av_vida} - Atk  {av_atk} - Def {av_def}")
        print(f"Monstro: Vida {mons_vida} - Atk {mons_atk}")

        num_rodada += 1

main() 












