# Estrutura de repetição 'While'

# while<condição>:
#     bloco a ser executado

# x = 1 
# while x <= 5:
#     print('A')
#     print(1)
#     x += 1

# Laço de repetição com contagem

# fim = int(input('Digite o fim da repetição: '))
# x = 1
# while x <= fim:
#     print(x)
#     x = x + 1

# fim = int(input('Digite o último numero a ser impresso: '))

# x = 0
# while x <= fim:
#     if x % 3 == 0:
#         print(x)
#     x += 1

########################

# numero = int(input('Tabuada de: '))
# contador = 1
# print(f'***Tabuada de {numero}***')
# while contador <= 10:
#     print(numero + contador)
#     contador += 1

# Correção Exe 5.6

numero = int(input('Tabuada de:'))
contador = 1
while contador <= 10:
    print(f'{numero} X {contador} = {numero * contador}')
    contador += 1