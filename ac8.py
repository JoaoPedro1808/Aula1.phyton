# AC8 - beecrowd 1028
def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

N = int(input())

for _ in range(N):
    F1, F2 = map(int, input().split())
    
    max_pilha = mdc(F1, F2)
    
    print(max_pilha)

# AC8 - beecrowd 1171
n = int(input())
contagem = {}

for _ in range(n):
    valor = int(input())
    contagem[valor] = contagem.get(valor, 0) + 1

for valor in sorted(contagem.keys()):
    print(f"{valor} aparece {contagem[valor]} vez(es)")

# AC8 - beecrowd 1329
while True:
    n = int(input())
    if n == 0:
        break
    
    results = list(map(int, input().split()))

    maria_wins = results.count(0)
    joao_wins = results.count(1)

    print("Mary won", maria_wins, "times and John won", joao_wins, "times")

# AC8 - beecrowd 1555
def r(x, y):
    return (3*x)**2 + y**2

def b(x, y):
    return 2*(x**2) + (5*y)**2

def c(x, y):
    return -100*x + y**3

def main():
    N = int(input())

    for _ in range(N):
        x, y = map(int, input().split())

        result_r = r(x, y)
        result_b = b(x, y)
        result_c = c(x, y)

        if result_r > result_b and result_r > result_c:
            print("Rafael ganhou")
        elif result_b > result_r and result_b > result_c:
            print("Beto ganhou")
        else:
            print("Carlos ganhou")

if __name__ == "__main__":
    main()
