"""
Creuza vai pegar um empréstimo no banco. 
O emprestimo que ela vai receber, vai ter que ser pago 20% de juros de volta. 
Ela também tem a opção de parcelar o pagamento de juros que ela pode oferecer.
"""
emprestimo = int(input("Quanto de empréstimo Creuza quer: R$"))

#Porcentagem do juros de Creuza
porcentagem_juros = 20

aumento_juros = (emprestimo*porcentagem_juros) / 100

juros_total = emprestimo + aumento_juros

print("")
decisao = int(input("Você quer parcelar o juros de Creuza? Sim[1] / Não[2]: "))

#Decisão se o usuário quiser parcelar:
if decisao == 1:
    print("")
    parcela = int(input("Em quantas vezes você quer parcelar o juros: x"))
    
    #Calculo do juros parcelado de Creuza:
    juros_parcelado = juros_total / parcela

    print(f"A parcela foi de: {parcela} vezes, então será cobrado R${juros_parcelado:.2f} por mês.")

#Decisão se o usuário não quer parcelar:
if decisao == 2:
    print("")
    print(f"O juros cobrado mensalmente será de: R${juros_total:.2f}")


    
