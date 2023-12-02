# km = int(input('Digite a distância que quer percorrer: '))
# valor = 0

# if km <= 200:
#     valor = km * 0.50
# else:
#     valor = km * 0.45

# print(f'O valor total da corrida foi de R${valor: .2f}')
##########################################################
# motorista = int(input('Digite de 1 a 5, qual o nível de motorista e carro você deseja: '))
# if motorista == 1:
#     preço = 1.25
# else:
#     if motorista == 2:
#         preço = 1.50
#     else:
#         if motorista == 3:
#             preço = 1.75
#         else:
#             if motorista == 4:
#                 preço = 2.00
#             else:
#                 if motorista == 5:
#                     preço = 3.00
#                 else:
#                     print('Por favor escreva um numero de 1 a 5')
#                     preço = 0.00
# if preço == 0.00:
#     exit(print('Nosso programa ainda não está finalizado então você vai ter que executar novamente o programa!'))
    
# km = int(input('Digite quantos km você vai andar: '))
# soma = km * preço

# print(f'Você irá pagar R${soma: .2f}, considerando o motorista mais o carro e a distância percorrida. Obrigado pela preferência!')

# Exercício 4.8

# numero1 = int(input('Digite o primeiro numero: '))
# numero2 = int(input('Digite o segundo numero: '))
# função = input('Escreva que função você quer fazer. Ex: "+" ; "-" ; "*" ; "/" : ')

# if função == '+':
#     soma = numero1 + numero2
# elif função == '-':
#     soma = numero1 - numero2
# elif função == '*':
#     soma = numero1 * numero2
# elif função == '/':
#     soma = numero1 / numero2
# print(f'O calculo final foi de: {soma}')

# Exercício 4.9

valorDaCasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
anosAPagar = int(input('Digite quantos anos vai parcelar: '))
anosAPagar = anosAPagar * 12
print(anosAPagar)
porcentagemSalario = salario * 0.30

prestação = valorDaCasa / anosAPagar

if prestação > porcentagemSalario:
    prestação = prestação - porcentagemSalario

print(f'O valor da prestação será de R${prestação: 0.2f}')