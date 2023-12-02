class Carro:
    cor = 'preto'
    marca = 'gol'
    modelo = 'top'

    def ligando_o_carro(self):
        print('Vrum, Vrum!!')

    def cor_do_carro(self):
        print(self.cor)

    def marca_do_carro(self):
        print(self.marca)

carrinho = Carro()
carrinho.cor = 'Vermelho'
carrinho.marca = 'Gol'
carrinho.modelo = 'Gti'
carrinho.cor_do_carro()
carrinho.marca_do_carro()
print(carrinho.modelo)
carrinho.ligando_o_carro()


print('#' * 20)
novo_carro = Carro()
novo_carro.cor_do_carro()
novo_carro.marca_do_carro()
print(novo_carro.modelo)
novo_carro.ligando_o_carro()