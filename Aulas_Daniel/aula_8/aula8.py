# valor = int(input("Digite o valor a pagar: "))
# cedulas = 0
# atual = 200
# apagar = valor

# while True:
#     if atual <= apagar:
#         apagar -= atual
#         cedulas += 1
#     else:
#         print(f"{cedulas} Cédulas de R${atual}")
#         if apagar == 0:
#             break
        
#         if atual == 200:
#             atual = 100
#         elif atual == 100:
#             atual = 50
#         elif atual == 50:
#             atual = 20
#         elif atual == 20:
#             atual = 10
#         elif atual == 10:
#             atual = 5
#         elif atual == 5:
#             atual = 2
#         elif atual == 2:
#             atual = 1
#         cedulas = 0

# Repetições Alinhadas

# tabuada = 1
# while tabuada <= 10:
#     numero = 1
#     while numero <= 10:
#         print(f"{tabuada} X {numero} = {tabuada * numero}")
#         numero += 1
#     tabuada += 1

# Repetições Alinhadas 2.0

# tabuada = 1
# fim_tabuada = int(input("Digite o fim da Tabuada: "))
# while tabuada <= fim_tabuada:
#     numero = 1
#     print(f"Tabuada de: {tabuada}")
#     while numero <= fim_tabuada:
#         print(f"{tabuada} X {numero} = {tabuada * numero}")
#         numero += 1
#     print(" ")
#     tabuada += 1

# Listas

# P[0], P[1] -> P[5]

# Lista = [1,2,3]
# print(Lista)
# Lista[0] = 20
# print(Lista)

# notas = [6, 7, 5, 8, 9]
# soma = 0
# x = 0
# while x < 5:
#     soma += notas[x]
#     x += 1
# print(f"Média:{soma / x: .2f}")

notas = [0,0,0,0,0]
soma = 0
x = 0
while x < 5:
    notas[x] = float(input(f"Digite a nota {x + 1}ª: "))
    soma += notas[x]
    x += 1
x = 0
print(" ")
print("Suas notas Bimestre a Bimestre")
while x < 5:
    print(f"Nota {x + 1}: {notas[x]: .2f}")
    x += 1
print(" ")
print(f"A sua média final: {soma / x : .2f}")
