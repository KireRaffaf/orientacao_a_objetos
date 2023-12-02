def contaDigito(n):
    return len( str(n) )
def exibe():
    n = int(input('Forneça um inteiro: '))
    print(contaDigito(n), ' dígitos')
    

exibe()