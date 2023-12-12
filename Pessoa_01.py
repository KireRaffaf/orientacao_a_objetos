class Pessoa():
    
    def __init__(self, nome, nascimento, cpf, rg, endereço, estado_civil):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__cpf = cpf
        self.__rg = rg
        self.__endereço = endereço
        self.__estado_civil = estado_civil

    @property
    def nome(self) -> str:
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def idade(self):
        idade = 2023 - self.__nascimento
        return idade
    
    @property
    def nascimento(self):
        return self.__nascimento
    @nascimento.setter
    def nascimento(self, nascimento):
        self.__nascimento = nascimento

    
    @property
    def cpf(self) -> int:
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    
    @property
    def rg(self) -> int:
        return self.__rg
    @rg.setter
    def rg(self, rg):
        self.__rg = rg 
    
    
    @property
    def endereço(self) -> str:
        return self.__endereço
    @endereço.setter
    def endereço(self, endereço):
        self.__endereço = endereço
    
    
    @property
    def estado_civil(self) -> str:
        return self.__estado_civil
    @estado_civil.setter
    def estado_civil(self, estado_civil):
        self.__estado_civil = estado_civil
    
    def tudo(self):
        print('Nome:',self.__nome)
        print('Idade:', pessoa.idade())
        print('Nascimento:',self.__nascimento)
        print('CPF:',self.__cpf)
        print('RG:',self.__rg)
        print('Endereço:',self.__endereço)
        print('Estado Civil:',self.__estado_civil)


# Pessoa(Idade, Nascimento, CPF, RG, Endereço, Estado Civil)    
pessoa = Pessoa('Erick', 2000, 000000000-00, 00000000-00, 'a', 'b')
nome = str(input('Digite o seu nome: '))
pessoa.nome = nome

nasc = int(input('Digite o ano do seu nascimento: '))
pessoa.nascimento = nasc

cpf = int(input('Digite o seu CPF: '))
pessoa.cpf = cpf

rg = int(input('Digite seu RG: '))
pessoa.rg = rg

endereço = str(input('Digite seu endereço: '))
pessoa.endereço = endereço

est_civil = str(input('Digite seu estado civil: '))
pessoa.estado_civil = est_civil

pessoa.tudo()