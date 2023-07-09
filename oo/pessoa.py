class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=58):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


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
    del charles.filhos
    charles.olhos = 1
    del charles.olhos
    print(charles.__dict__)
    print(lucas.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(charles.olhos)
    print(lucas.olhos)
    print(id(Pessoa.olhos), id(charles.olhos), id(lucas.olhos))
    print(Pessoa.metodo_estatico(), charles.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), charles.nome_e_atributos_de_classe())

