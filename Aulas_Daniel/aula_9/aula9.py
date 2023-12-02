#                       Aula 09

# for x in [5,6,7,8,9,10]:
#     print(x)

# for x in range(0,20,5):
#     print(x)

# lista = [8,9,15]

# for e in lista:
#     print(e)

# lista = ["Erick", "Julio", "Li"]

# for e in lista:
#     print(e)

# x = 0

# while x < len(lista):
#     e = lista[x]
#     print(e)
#     x += 1

# lista = [7, 9, 10, 12]

# p = int(input("Digite um número a pesquisar: "))

# for e in lista:
#     if e == p:
#         print('Elemento encontrado')
#         break
#     else:
#         print('Elemento não encontrado')

# for imprime9 in range(10):
#     print(imprime9)


# for t in range(3, 33, 3):
#     print(t, end=' ')
# print()

# from time import sleep

# for par in range(2,51,2):
#     print(par, end=' ')
#     sleep(0.5)
# print('\nNúmeros pares até 50.....')

#####################
# Para == for

# for i in range(0,10):
#     print(i+1)
# print('Fim')

# for i in range(10,-1 ,-1):
#     print(i)
# print('fim')

# numero = int(input('Digite um número: '))
# for i in range(0, numero+1):
#     print(i)
# print('Fim')

# inicio = int(input('Digite um número: '))
# fim = int(input('Digite o fim: '))
# passo = int(input('Digite o passo: '))

# for i in range(inicio, fim+1, passo):
#     print(i)
# print('Fim')

# soma = 0 
# fim = int(input('Digite quantos números deseja somar: '))
# for i in range(0,fim):
#     numero = int(input('Digite um valor: '))
#     soma += numero
# media = soma/fim
# print(f'A soma dos números foi: {soma}, e media foi {media: .2f}')

from time import sleep
for i in range(10, -1 , -1):
    print(i)
    sleep(1)
print('Apitou, começou!!!!!')