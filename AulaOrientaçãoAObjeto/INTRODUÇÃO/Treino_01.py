class Carro:
    cor = "Preto"
    marca = "A mais top"
    modelo = "Top 1"
    def ligar_a_potência(self):
        x = 0
        print("Ligando o carro")
        while x <= 5:
            sleep(1)
            texto = x * '.' 
            print(f'{texto}')
            x += 1
        print("Vrum, vrum!!!")
from time import sleep

carrinho = Carro()
print(carrinho.marca)
carrinho.ligar_a_potência()
print("Finalmente minha potência ligou!")