class Pessoa:
    def __init__(self, *filhos, nome=None, idade=58):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    lucas = Pessoa(nome='Lucas', idade=29)
    charles = Pessoa(lucas, nome='Charles')
    print(Pessoa.cumprimentar(charles))
    print(id(charles))
    print(charles.cumprimentar())
    print(charles.nome)
    print(charles.idade)
    for filho in charles.filhos:
        print(filho.nome)
    charles.sobrenome='Weller'
    del lucas.filhos
    print(charles.__dict__)
    print(lucas.__dict__)

