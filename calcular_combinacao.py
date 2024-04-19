m = int((input("Informe o M: ")))
n = int((input("Informe o N: ")))
k = m - n

def fatorial(m):
    if m == 1:
        return 1
    return m * fatorial(m - 1)

def fatorial2(n):
    if n == 1:
        return 1
    return n * fatorial2(n - 1)

def fatorial3(k):
    if k == 1:
        return 1
    return k * fatorial3(k - 1)

m1 = fatorial(m)
k1 = fatorial3(k)
n1 = fatorial(n)


def combinacao(m1, k1, n1):
    return m1 // (n1 * k1)

print(combinacao(m1, n1, k1))






