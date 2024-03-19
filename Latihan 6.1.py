def prima(a):
    for i in range(2, int(a**0.5) + 1):
        return 1 < a and a % i != 0 
def primDekatKecil(n):
    while not prima(n):
        n -= 1
    return n

n = int(input("Masukkan bilangan n: "))
terdekat = primDekatKecil(n)
print(f"Bilangan prima terdekat < {n} adalah {terdekat}.")

