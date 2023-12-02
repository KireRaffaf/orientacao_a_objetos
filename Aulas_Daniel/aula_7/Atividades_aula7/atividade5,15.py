x = 0
print("Olá, tudo bem? Você tem que terá que digitar de 1,2,3,5 e 9 pra decidir qual produto irá levar.")
print("1 - R$0,50\n2 - R$1,00\n3 - R$4,00\n5 - R$7,00\n9 - R$8,00")
saldo = 0
while True:
    num = int(input("Digite o código: "))
    if num == 0:
        break
    elif num == 1:
        saldo += 0.50
    elif num == 2:
        saldo += 1
    elif num == 3:
        saldo += 4
    elif num == 5:
        saldo += 7
    elif num == 9:
        saldo += 8
    else:
        print('Codigo inválido! Insira o codigo novamente.')
        x -= 1
    x += 1
print(f'A quantidade de produtos comprados foi de {x} produtos.')
