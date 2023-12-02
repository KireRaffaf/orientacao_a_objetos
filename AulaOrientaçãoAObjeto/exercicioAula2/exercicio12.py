# ler 2 string - printar e printar a quantidade de caracter - comparar pra ver se ambas possuem o mesmo tanto de caracters

def contaDigito1(a):
    soma = len(str(a))
    # soma1 = len(str(b))
    return soma
def contaDigito2(b):
    soma = len(str(b))
    return soma

    
    
def exibe():
    a = int(input('Forneça um inteiro: '))
    b = int(input('Forneça um inteiro: '))
    contDigit = contaDigito1(a)
    contDigit2 = contaDigito2(b)
    print(f'{contDigit} , {contDigit2} digitos')
    
    
    

exibe()




