# Exercicio 5.1

# x = 1

# while x <= 99:
#     x = x + 1
#     print(f'{x}')

# Exercicio 5.2

# contagem = 50

# while contagem <= 100:
#     print(contagem)
#     contagem += 10

# Exercicio 5.3

# regresso = 10
# while regresso >= 0:
#     print(regresso)
#     regresso -= 1
# print('Fogo!')

# Exercicio 5.4

# fim = int(input('Digite um numero: '))
# x = 0

# while x <= fim:
#     if x % 3 == 0:
#           print(x)
#     x += 1


# x = 1

# while x <= 30:
#     if x % 3 == 0:
#           print(x)
#     x += 1

# x = 1 

# fim = int(input('Digite até que número quer contar: '))

# while x <= fim:
#     if x % 2 == 0:
#         print(f'{x} Par')
#     else:
#         print(f'{x} Impar')
#     x += 1


# Exercicio 5.6 

# numero = 2
# contador = 1
# print(f'***Tabuada de {numero}***')
# while contador <= 10:
#     print(f' {numero} x {contador} = {numero * contador}')
#     contador += 1

# Exercicio 5.7

# numero = 2
# inicio = int(input('Digite o inicio da tabuada: '))
# fim = int(input('Digite o fim da tabuada: '))

# while inicio <= fim:
#     print(numero * inicio)

#     inicio += 1

# Exercicio 5.8

# numero1 = int(input('Digite o primeiro numero: '))
# numero2 = int(input('Digite o segundo numero: '))
# soma = 0
# x = 1

# while x <= numero1:
#     soma = soma + numero2
#     x = x + 1

# print(f'{numero1} x {numero2} = {soma}')

# Atividade 5.9

# numero1 = int(input('Digite o primeiro numero: '))
# numero2 = int(input('Digite o segundo numero: '))
# x = 0
# soma = 0
# while soma < numero1:
#     x = x + 1
#     soma += numero2
    

# print(f'{numero1} / {numero2} = {x}')

numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
x = 0
y = numero1
subtração = numero1
numero1 -= 1
while subtração > numero1:
    x = x + 1
    subtração -= numero2
    numero1 = 0

    

print(f'{y} / {numero2} = {x}')