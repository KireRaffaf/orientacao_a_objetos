def diferença():
    x = float(input('Digite um numero real: '))
    y = float(input('Digite um outro numero real: '))
    if x > y:
        print(f'O valor {x} é o maior.')
    elif x == y:
        print('Os dois tem o mesmo valor.')
    else:
        print(f'O valor {y} é o maior.')

diferença()
