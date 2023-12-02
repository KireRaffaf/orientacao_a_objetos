#Resposta livro/Prof

deposito = float(input("Depósito inicial: "))
taxa = float(input('Taxa de juros (Ex.: 3 para 3%): '))
investimento = float(input('Digite o depósito mensal: '))
mes = 1
saldo = deposito

while mes <= 24:
    saldo = saldo + (saldo * (taxa/100) + investimento)
    print(f"Saldo do mes {mes} é de R${saldo: .2f}")
    mes = mes + 1
    deposito += investimento
print(f"O ganho obtido com os juros foi de R${saldo - deposito : .2f}")