class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.__ano = ano
        self.__duracao = duracao
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.__ano = ano
        self.__temporadas = temporadas
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

filme = Filme("top gun: Maverick", 2022, 160)
serie = Serie("gothan", 2017, 8)

print(f"Filme: {filme.__nome} - Ano: {filme.__ano} - Duração: {filme.__duracao} - Likes {filme.__likes}")
print(f"Serie: {serie.__nome} - Ano: {serie.__ano} - Temporada: {serie.__temporadas} - Likes {serie.__likes}")