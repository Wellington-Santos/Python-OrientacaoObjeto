## Exemplo de mutabilidade de uma lista:

def faz_processamento_de_visualizacao(lista):
    print(len(lista))

idades = [16, 21, 29, 56, 43]
faz_processamento_de_visualizacao(idades)
print(idades)

## Temos um método que retona o tamanho de uma lista para o usuário, porem o que acontece se no meio do método colocarmos um "append" na lista?
def faz_processamento_de_visualizacao_mod1(lista):
    print(len(lista))
    lista.append(13)

faz_processamento_de_visualizacao_mod1(idades)
print(idades)
## A mudança nesse método ele pode acresentar mais um valor na lista, mesmo ele exibindo que tem 5 elementos dentro da lista que foi passada para o método
## para resolver isso nos podemos alterar o nosso metodo para que toda vez ele tenha uma lista vazia, assim:

def faz_processamento_de_visualizacao_mod2(lista = []):
    print(len(lista))
    lista.append(13)

faz_processamento_de_visualizacao_mod2()
faz_processamento_de_visualizacao_mod2()
faz_processamento_de_visualizacao_mod2()

## Se verificarmos bem ele está aumentado o valor da nossa lista mesmo passando para ele que essa lista por default e vazia, isso acontece pois essa lista está instanciada na memoria,
## e quando esse metodo e executado pela primeira vez, ele instancia essa lista uma vez e nas outras vezes ele vai realizando o append, pois a lista ja exite na memoria.
## para resolver isso temos que passar a lista como None e fazer uma tratativa caso esse parametro esteja vazio, assim:

def faz_processamento_de_visualizacao_mod3(lista = None):
    if lista == None:
        lista = list()
    print(len(lista))
    lista.append(13)

faz_processamento_de_visualizacao_mod3()
faz_processamento_de_visualizacao_mod3()
faz_processamento_de_visualizacao_mod3()

## Dessa maneira, a lista instanciada na memória e do tipo None, sendo assim, no método eu realizo uma verificação se for None, eu crio uma lista nova, se não eu uso a lista que foi passada como parametro

## Obs.: Lembrando que essa tratativa e para quando formos trabalhar com lista e objetos mutaveis