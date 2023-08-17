"""
def soma(x,y):
    return x + y

print(soma(2,3))
print(soma(31, 45))
"""

"""
def somav1v2(x, y):
    return x + y
v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))
s = somav1v2(v1, v2)

print("A soma dos dois números é de:", s)
"""

def ParOuImpar(v):
    if (v % 2 == 0):
        return ("Par")
    else:
        return ("Impár")

n = int(input("Digite um número: "))
r = ParOuImpar(n)
print("O número", n, "é um número", r)



