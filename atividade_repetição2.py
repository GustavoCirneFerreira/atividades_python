"""
cont = 1
s = 0
resp = "S"

while (resp == "S"):
    n = int(input("\nDigite um número para fazer a soma. "))
    s = s + n
    resp  = input("\nQuer continuar? [S]/[N] ")
else:
    print("A soma foi de : " , s)   
"""
"""
cont = 1
n = 5
r = n * cont

while (cont <= 10):
     print(n, "x", cont, "=", r)
     cont = cont + 1
     r = n * cont
"""

"""
n = int(input("DIGITE UM NÚMERO: "))    
cont = n
f = 1

while (cont >= 1):
    print(cont, "x")
    f = f * cont
    cont = cont - 1
print("O número fatorial de", n, "é de:", f)
"""

"""
n = int(input("DIGITE UM NÚMERO: "))
cont = 1
contdiv = 0

while (cont <= n):
    print(cont)
    cont = cont + 1
    
    if (contdiv > 2):
        contdiv = contdiv + 1
print("O número é primo!")

else:
print("O valor é um numero primo!")
"""

cont = 1
cont2 = 10
print("----------------------------------------")
print("|            SUPERCONTADOR             |")
print("----------------------------------------")
print("|          [1] de 1 até 10             |")
print("|          [2] de 10 até 1             |")
print("|          [3] para sair.              |")
print("----------------------------------------")

while True:
    esc = int(input("\n Escolha entre essas três opções: "))
    if (esc == 1):
        while (cont <= 10):
            print(cont)
            cont = cont + 1

    elif (esc == 2):
        while (cont2 >= 1):
            print(cont2)
            cont2 = cont2 - 1

    elif (esc == 3):
        print("Até a próxima!")
        break

            


