## Declaração das variaveis no qual será a base da nossa lista.
# idade1 = 15
# idade2 = 30
# idade3 = 27
# idade4 = 18

## Uma forma simples de exibir os valores declarados, porém essa e uma forma mais trabalhosa de se lidar,
## pois caso temos que inserir algum novo item teremos que tanto declarar a variavel manualmente quanto exibir o valor manualmente.

# print(idade1)
# print(idade2)
# print(idade3)
# print(idade4)

## Essa e uma maneira simples de montar uma lista, nela podemos exibir todos os itens nela mais facil do que anteriormente.
idades = [15,30,27,18]
print("Exibindo a Lista de idades: ", idades)

## Verificando o tipo da lista:
print("\nTipo da Lista: ", type(idades))

## Verificando o tamanho da lista:
print("\nTamanho da Lista: ", len(idades))

## Exibindo um valor específico da lista:
print("\nNa posição {} tem a idades: {}".format(0,idades[0]))
print("\nNa posição {} tem a idades: {}".format(3,idades[3]))

## Podemos realizar loops de interação com a lista:
for idade in idades:
    print("Loop de interação exibindo a idades: ", idade)

## Caso precise de inserir algum valor novo na lista temos duas maneiras de fazer isso:
## 1° Usando o metodo "append" conforme abaixo, porém ele adicionar os novos valores no final da lista:
idades.append(19)
idades.append(22)
print("\nAdicionando nos valores no Final da Lista: ", idades)

## 2° Usando o metodo "insert", nele informamos em qual trecho da lista queremos inserir o novo valor:
idades.insert(0,21)
idades.insert(0,23)
print("\nAdicionando novos valores no inicio da Lista: ", idades)
## Obs.: no metodo "insert", informamos dois valores, qual posição da lista vamos inserir e o novo valor,
## caso a posição seja 0 o novo valor será inserido no inicio da lista, antes de todos os valores

## Tem podemos remover itens da nossa lista:
idades.remove(19)
print("\nRemovendo a idade 19 da Lista: ", idade)

## caso tente remover o item 19 de novo da lista, dará erro, pois o item 19 não existe
# idades.remove(19)

## Para resolver o erro acima, podemos verificar se o item existe antes de remove-lo
if 19 in idades:
    idades.remove(19)

print("\nVerificando se a idade 19 está na Lista: ", idade)
## Dessa maneira o código irá verificar se o item existe na lista, caso exista ele remove, senão segue o fluxo normalmente.


## Agora, caso queria remover na lista valores repetidos, o metodo "remove" exluir apenas a primeira apariçao do valor na lista
## Ex.: A idade 15 está no inicio da lista, irei adicionar a idade 15 no final da lista e irei remove-la
idades.append(15)
idades.remove(15)
print("\nRemovendo idades repetidas na Lista: ", idades)

## Veja que o metodo removeu a idade 15 que estava no inicio da lista e a idade 15 ficou apenas no final da lista

## Caso você queira adicionar mais de um valor na lista, o metodo "append" não suporta, pois ele precisa apenas de um parametro
## Evite de realizar um append mais uma lista Ex.:
idades2 = idades.copy()
idades2.append([39,40])
print("\nAdicionando uma lista dentro de uma lista: ",idades2)

## Perceba que na lista os valores, 39 e 40 ficaram de um lista dentro da lista de idades e não e isso queria realizar, para solucionar isso
## usaremos o metodo "extend" que ele pegar os valores/elementos uma lista e adionar em outra Ex.:
idades.extend([39,40])
print("\nUsando o método 'extend' para dicionar valores/elementos de uma lista em outra ", idades)

## Caso queira montar uma outra lista com idades + 1 anos, podemos seguir dessa forma
idades_ano_que_vem = []
for idade in idades:
    idades_ano_que_vem.append(idade + 1)
print("\nLista com idades daqui há um ano: ", idades_ano_que_vem)

## uma outra maneira de fazer esse mesmo metodo mais simples e que antes do for infomamos que para cada idades adicione + 1 Ex.:
idades_ano_que_vem_2 = [(idade + 1) for idade in idades]
print("\nSimplificando a maneira de adicionar um ano a mais nas idades: ", idades_ano_que_vem_2)

## dessa outra maneira também podemos realizar filtragem de valores Ex.: Irei filtrar apenas valores acima de 25 anos
idades_filtradas = [(idade) for idade in idades if idade > 25]
print("\nFiltrando a Lista e trazendo as idades acima de 25 anos: ", idades_filtradas)

## Essa a maneira de montar a lista dessa maneira se chama Lista Comprehension
