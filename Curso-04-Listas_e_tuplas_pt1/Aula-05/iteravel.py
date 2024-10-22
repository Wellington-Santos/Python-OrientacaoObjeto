#Objetivo e mostrar a idade e em qual posição ela está
idades = [18, 87, 32, 65, 56, 32, 49, 37]

# #Aqui ele so mostra a idade
# for idade in idades:
#     print(idade)

#Usando o range para exibir idade e posição na lista
# for i in range(len(idades)):
#     print(i, idades[i])

# Usando o enumerate 
# print(list(enumerate(idades))) #Forçando a enumeração pelo enumerate usando o instanciamento da lista

#Desenpacotamento da lista
for indice, valor in enumerate(idades):
    print(indice, "x", valor)

print("\n\n")

usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]

for nome, idade, nascimento in usuarios:
    print(nome, idade)

print("\n\n")

print(sorted(idades))

print("\n")

print(list(reversed(idades)))

print("\n")

print(sorted(idades, reverse=True))
