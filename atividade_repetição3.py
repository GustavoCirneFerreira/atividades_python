"""
v = int(input("Digite um valor: "))

if (v % 2 == 1):
    v = v - 1
for cont in range(v, 0, -2):
    print(cont)
"""

tot10 = 0
SImp = 0
for cont in range(1, 6):
    v = int(input("Digite um valor: "))

    if (v <= 10) and (v >= 0):
        tot10 = tot10 + 1
        if (v % 2 == 1):
            SImp = SImp + v
print("\nAo total, foi cerca de", tot10, "valores entre 0 e 10.\n")
print("A soma dos valores ímpares é de:", SImp)

