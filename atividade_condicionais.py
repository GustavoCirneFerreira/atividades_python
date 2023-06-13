"""
#Maior ou menor de idade:

ano = (int(input('Em que ano estamos? ')))
nascimento = (int(input('Em que ano você nasceu? ')))

idade = ano - nascimento
if (idade >= 18):
    print(f'Em {ano} você tem {idade} anos. Nessa época você é maior de idade.')
else: 
    print(f'Em {ano} você tem {idade} anos. Nessa época você é menor de idade.')
"""

"""
#Par ou ímpar:


N1 = int(input('Digite um número: '))
if (N1 % 2 == 0):
    print(f'O número {N1} é par.')
else:
    print(f'O número {N1} é ímpar.')
"""
"""
#IMC:

altura = float(input(f'Qual é a sua altura? '))
peso = float(input('Qual é o seu peso? '))

imc = peso / (altura ** 2)

print(f'{imc:.2f}\r')

if (imc >= 18.5) and (imc <= 25):
    print('Você está com o IMC em média. Parábens!')
else:
    print('Você está com o IMC fora da média. Mantenha o seu IMC em cheque.')
"""

print('--------------------------------------------\r')
print('     DEPARTAMENTO DE TRÂNSITO\r')
print('--------------------------------------------\r')

ano_nasc = int(input('Em que ano você nasceu? '))
ano = int(input('Em que ano estamos? '))

idade = ano - ano_nasc

if (idade >= 18):
    print('Parabéns! Está apto para providenciar sua carteira de motorista!')
else:
    print('Não está inapto para ser providenciado uma carteira de motorista.')
