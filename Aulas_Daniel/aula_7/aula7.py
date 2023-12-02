# pontos = 0
# questão = 1
# while questão <= 3:
#     resposta = input(f'Resposta da questão {questão}: ')
#     if questão == 1 and resposta == 'b' or resposta == 'B':
#         pontos += 1
#     if questão == 2 and resposta == 'a' or resposta == 'A':
#         pontos += 1
#     if questão == 3 and resposta == 'd' or resposta == 'D':
#         pontos += 1
#     questão += 1
# print(f'O aluno fez {pontos} ponto(s)')

# Acumuladores

# contador = 1
# soma = 0

# while contador <= 10:
#     numero = int(input(f'Digite o {contador}° número: '))
#     soma += numero
#     contador += 1
# print(f'Soma: {soma}')

# x = 1
# soma = 0 
# while x <= 5:
#     n = int(input(f'{x} Digite o Número: '))
#     soma = soma + n
#     x = x + 1
# print(f'Média : {soma / 5 :.2f}')

# Interrompendo a repetição

s = 0
while True:
    v = int(input("Digite um número a somaar ou 0 para sair: "))
    if v == 0:
        break
    s += v
print(s)