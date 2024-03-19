def faktor(n):
    return 1 if n == 0 else n * faktor(n-1)

def piramid(n):
    for i in range(n, 0, -1):
        print(faktor(n), end=" ")
        for j in range(n, n-i, -1):
            print(j, end=" ")
        print()

n = int(input("Masukkan nilai n: "))
piramid(n)
