# #Codigo sobre o imposto
# salario = float(input('Digite o salario para calculo do Imposto: '))
# base = salario
# imposto = 0
# if base > 3000:
#     imposto = imposto + ((base - 3000) * 0.35)
#     base = 3000
# print(imposto)
# if base > 1000:
#     imposto = imposto + ((base - 1000) * 0.20)
# print(imposto)
# print(f'Salário: R${salario: 6.2f} Imposto a pagar: R${imposto: 6.2f}')

#Codigo sobre idade

# idade = int(input('Digite a idade do seu carro: '))
# if idade <= 3:
#     print('Seu carro é novo')
# else:
#     print('Seu carro é velho!!')

#Codigo sobre distancia

#Codigo sobre if's de minutos

# minutos = int(input('Quantos minutos você utilizou esse mês: '))
# if minutos < 200:
#     preço = 0.20
# else:
#     if minutos < 400:
#         preço = 0.18
#     else:
#         preço = 0.15
# print(f'Você vai pagar este mês: R${minutos * preço: .2f}')

# Codigo sobre varios if's com categoria

# categoria = int(input('Digite a categoria do produto: '))
# if categoria == 1:
#     preço = 10
# else:
#     if categoria == 2:
#         preço = 18
#     else:
#         if categoria == 3:
#             preço = 23
#         else:
#             if categoria == 4:
#                 preço = 26
#             else:
#                 if categoria == 5:
#                     preço = 31
#                 else:
#                     print('Categoria inválida, digite um valor entre 1 e 5!')
#                     preço = 0
# print(f'O preço do produto é: R${preço: .2f}')

# Resolução da atividade de bandeira

# distancia = int(input('Digite a distancia percorrida: '))
# bandeira = int(input('Digite a bandeira: '))

# if bandeira == 1:
#     if distancia < 200:
#         preço_corrida = (distancia * 2) * bandeira
#     else:
#         preço_corrida = (distancia * 1.75) * bandeira

# else:
#     if bandeira == 2:
#         if distancia < 200:
#             preço_corrida = (distancia * 2) * bandeira
#         else:
#             preço_corrida = (distancia * 1.75) * bandeira
#     else:
#         print('Bandeira invalida! Digite 1 ou 2 para bandeira')
# print(f'O total a ser pago pela corrida será: R${preço_corrida: .2f}')

# Codigo de categoria com ELIF

# categoria = int(input('Digite a categoria do produto: '))

# if categoria == 1:
#     preço = 10
# elif categoria == 2:
#     preço = 18
# elif categoria == 3:
#     preço = 23
# elif categoria == 4:
#     preço = 26
# elif categoria == 5:
#     preço = 31
# else:
#     print('Categoria inválida, digite um valor entre 1 a 5')
#     preço = 0
# print(f'O preço do produto é: R${preço: .2f}')