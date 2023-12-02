deposito = float(input('Digite a quantidade que quer depositar: '))
taxa = float(input('Digite a taxa de juros: '))
mesês = 1
soma = deposito

while mesês <= 24:
    soma += soma * taxa / 100
    mesês += 1
print(f'O total de juros acumulados em reais foi de: R${soma-deposito:.2f}')

#Resposta livro/professor

# deposito = float(input("Depósito inicial: "))
# taxa = float(input('Taxa de juros (Ex.: 3 para 3%): '))
# mes = 1
# saldo = deposito

# while mes <= 24:
#     saldo = saldo + (saldo * (taxa/100))
#     print(f"Saldo do mes {mes} é de R${saldo: .2f}")
#     mes = mes + 1
# print(f"O ganho obtido com os juros foi de R${saldo - deposito : .2f}")