"""
N1 = float(input('Escreva a primeira nota: \n'))
N2 = float(input('Escreva a segunda nota: \n'))

media = (N1 + N2) / 2

if (media >= 7):
    print(f'Sua média:  {media:.2f}')
    print('Parabéns! o aluno foi APROVADO.')

elif (media >= 5) and (media < 7):
    print(f'Sua média:  {media:.2f}')
    print('O aluno está em RECUPERAÇÃO.')

#Não é necessário dizer a condição. Já que logicamente é a única possibilidade 
#de algo acontecer caso a condição não caia en nenuhuma das anteriores:    
else:
    print(f'Sua média:  {media:.2f}')
    print('A média está abaixo do mínimo (4.0). O aluno foi REPROVADO.')
"""   
"""
print('--------------------------------------')
print('         CÁLCULO IMC')
print('--------------------------------------')
alt = float(input('Qual é a sua altura?\n'))
peso = float(input('E seu peso? \n'))

imc = peso / (alt * 2)

if (imc < 17):
    print('----------------------------------')
    print('     IMC:')
    print(f'     {imc:.2f}')
    print('     STATUS:')
    print('     Muito abaixo do peso.')
    print('----------------------------------')

elif (imc >= 17) and (imc < 18.5):
    print('----------------------------------')
    print('     IMC:')
    print(f'     {imc:.2f}')
    print('     STATUS:')
    print('     Abaixo do peso.')
    print('----------------------------------')

elif (imc >= 18.5) and (imc < 25):
    print('----------------------------------')
    print('     IMC:')
    print(f'     {imc:.2f}')
    print('     STATUS:')
    print('     Peso ideal.')
    print('----------------------------------')

elif (imc >= 25) and (imc < 30):
    print('----------------------------------')
    print('     IMC:')
    print(f'     {imc:.2f}')
    print('     STATUS:')
    print('     Sobrepeso.')
    print('----------------------------------')

elif (imc >= 30) and (imc < 35):
    print('----------------------------------')
    print('     IMC:')
    print(f'     {imc:.2f}')
    print('     STATUS:')
    print('     Obesidade.')
    print('----------------------------------')

elif (imc >= 35) and (imc < 40):
    print('----------------------------------')
    print('     IMC:')
    print(f'     {imc:.2f}')
    print('     STATUS:')
    print('     Obesidade severa.')
    print('----------------------------------')

elif (imc >= 40) and (imc < 100):
    print('----------------------------------')
    print('     IMC:')
    print(f'     {imc:.2f}')
    print('     STATUS:')
    print('     Obesidade mórbida.')
    print('----------------------------------')
"""

print('------------------------------------')
print('          CRIANÇA ESPERANÇA         ')
print('------------------------------------')
print('\n')
print('Muito obrigado por nos escolher para doar por uma causa.\n')
print('-------------------------------------')
print('          DOAÇÕES:         ')
print('Digite [1] para doar R$10.00.')
print('Digite [2] para doar R$25.00.')
print('Digite [3] para doar R$50.00.')
print('Digite [4] para doar selecionar o valor.')
print('Digite [5] para doar cancelar a doação.')
print('------------------------------------\n')
D = int(input('->'))


if (D == 1):
    Valor = 10.00

elif (D == 2):
    Valor = 25.00

elif (D == 3):
    Valor = 50.00

elif (D == 4):
    Valor = float(input('Digite seu valor desejado: R$'))

elif(D == 5):
    Valor = 0

print('------------------------------------------------')
print(f'          SUA DOAÇÃO FOI DE: R${Valor:.2f}     ')
print('           Muito obrigado por nos escolher.')
print('------------------------------------------------')



    






    
    


