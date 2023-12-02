media = 0
x = 0
soma = 0
while True:
    num = int(input('Digite um valor a somar: '))
    if num == 0:
        break
    x += 1
    soma += num
media = x
media = soma / media
print(f"O total de números digitados para somar foi {x}. A soma foi de {soma} e o resultado da média aritmética e {media}")