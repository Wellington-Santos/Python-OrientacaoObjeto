from collections import defaultdict
from collections import Counter

texto_exemplo = "Bem vindo meu nome é Wellington e eu gosto muito de nomes e tenho o meu cachorro e gosto muito de papagaios"
texto_split = texto_exemplo.split()

# print(texto_split)

aparicoes = {}
aparicoes_default = defaultdict(int) 

aparicoes_teste = {
    "Wellington": 1,
    "papagaio": 2,
    "nome": 2,
    "vindo": 1
}

# print(aparicoes_teste.get("xpto", 0))

# print(aparicoes_teste.get("papagaio", 0))

# Adicionando item no dicionário
aparicoes_teste["beto"] = 5
# print(aparicoes_teste)

del aparicoes_teste["beto"]
# print(aparicoes_teste)

# print(["Palavra {}".format(chave) for chave in aparicoes_teste.keys( )])

for palavra in texto_exemplo.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)

for palavra in texto_exemplo.split():
    aparicoes_default[palavra] += 1

print(aparicoes_default)

class Conta:
    def __init__(self):
        print("Criando uma conta")

contas = defaultdict(Conta)

contas[15]

aparicoes_counter = Counter(texto_exemplo.split())

print(aparicoes_counter)
