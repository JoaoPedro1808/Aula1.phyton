#AC9 - beecrowd 1016
n = int(input())

n *= 2

print(f"{n} minutos")

#AC9 - beecrowd 1153
n = int(input())

for i in range(1, n):
    n *= i

print(n)

#AC9 - beecrowd 1281
def main():
    N = int(input())

    for _ in range(N):
        M = int(input())
        frutas = []
        precos = []

        for _ in range(M):
            fruta, preco = input().split()
            frutas.append(fruta)
            precos.append(float(preco))

        P = int(input())
        resposta = 0.0

        for _ in range(P):
            fruta, quantidade = input().split()
            quantidade = int(quantidade)

            for j in range(M):
                if fruta == frutas[j]:
                    resposta += quantidade * precos[j]
                    break

        print("R$ {:.2f}".format(resposta))

if __name__ == "__main__":
    main()

#AC9 - beecrowd 2006
n = int(input())
m = list(map(int, input().split(" ")))

print(m.count(n))

#AC9 - beecrowd 2339
c, p, f = map(int, input().split(" "))

def aviao_de_papel(c, p, f):
    if p >= c * f:
        print("S")
    else:
        print("N")

aviao_de_papel(c, p, f)

#AC9 - beecrowd 2388
N = int(input())
distancia = 0

for i in range(N):
    T, V = map(int, input().split(" "))
    distancia += T * V

print(distancia)

#AC9 - beecrowd 2413
t = int(input())

t *= 4

print(t)

#AC9 - beecrowd 3048
N = int(input())
sequencia = [int(input()) for _ in range(N)]

consecutivos = 1 
atual = sequencia[0]

for i in range(1, N):
    if sequencia[i] != atual:
        consecutivos += 1
    atual = sequencia[i]

print(consecutivos)
