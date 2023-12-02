def mês_por_extenso(d,m,a):
    mês = {1: 'janeiro' , 2: 'fevereiro' , 3: 'março' , 4:'abril' , 5: 'maio' , 6: 'junho' , 7: 'julho' , 8: 'agosto' , 9: 'setembro' , 10: 'outubro' , 11: 'novembro' , 12: 'dezembro'}
    soma = f'{int(d)} de {mês[m]} de {int(a)}'
    return soma
        
    
print('Escreva a data com o formato de XX/X/XXXX')
dia = int(input('Digite um dia: '))
mes = int(input('Digite um mês: '))
ano = int(input('Digite um ano: '))

if 00 == dia or 32 <= dia or 0 == dia:
    print('Ocorreu um erro na digitação do dia, tente novamente!')
elif 0 == mes or 13 <= mes:
    print('Ocorreu um erro na digitação do mês, tente novamente!')
elif 0000 == ano or 999 >= ano or 9999 < ano:
    print('Ocorreu um erro na digitação do ano, tente novamente!')
else:
    mês_ext = mês_por_extenso(dia,mes,ano)
    print(mês_ext)



    