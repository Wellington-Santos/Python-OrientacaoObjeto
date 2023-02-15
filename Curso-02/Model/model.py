# Definição da Classe Pai, que terá atributos e métodos herdados pelas classes filhas 
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @property
    def likes(self):
        return self._likes

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    # Método para realizar uma interpretação textual do objeto, independente dos atributos que haverá nas classes filhas
    def __str__(self):
        return f"{self._nome} - {self.ano} - {self._likes} Likes"

# Definição das classes filhas e seus atributos particulares
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    # Observe que neste método, estou realizando uma sobrecarga do método que está na classe pai, com os atributos específicos dessa classe
    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.duracao} min - {self.likes} Likes"

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} Likes"

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas


    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)
    

filme = Filme("top gun: Maverick", 2022, 160)
filme2 = Filme("todo mundo em pânico", 1998, 100)
serie = Serie("gothan", 2016, 8)
serie2 = Serie("Demolidor", 2018, 6)

filme.dar_like()
filme.dar_like()

filme2.dar_like()
filme2.dar_like()
filme2.dar_like()

serie.dar_like()

serie2.dar_like()
serie2.dar_like()
serie2.dar_like()



playlist = [filme, serie, filme2, serie2]

programacao = Playlist("Programação Fim de Semana", playlist)

print(f"Tamanho da playlist {len(playlist)}")

for programa in programacao:
    # A partir do momento que já tenho um método para realizar interpretação textual da classe declarado no objeto, eu posso simplesmente dar um print nele, que ele irá trazer as informações do objeto
    print(programa)

