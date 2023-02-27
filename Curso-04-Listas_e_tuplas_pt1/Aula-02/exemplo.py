## Criação de uma classe para exemplificar o uso de tuplas, objetos e anemia

## Definimos uma classe base que terás alguns atributos e metodos referente a contas
class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)
    
    def deposita(self, valor):
        self.saldo += valor

## Instanciamos a classe e chamamos o metodo deposita, para adicionar nas contas um valor inicial
conta_wellington = ContaCorrente(15)
conta_wellington.deposita(50)

conta_fulano = ContaCorrente(35)
conta_fulano.deposita(1000)

## Por conta do método "__str__" que esta dentro da classe conseguimos exibir um texto padrão com as informações de contas.

print("Informações da conta Wellington: ", conta_wellington)
print("Informações da conta Fulano: ", conta_fulano)

## Depois de termos criados as instancias de contas e depois de ver o resultado, adicionaremos as instancias das contas ja criadas, para uma lista de contas.
# nela, conseguimos chamar o metodo deposita, por cada posição da conta dentro da lista. Ex.:    
contas = [conta_wellington, conta_fulano]

## Dessa maneira irá exibir o valor da conta de fulano
print("Informações dentro da Lista de Contas, posição 0 ", contas[0])


## Criação de um método para realizar o deposito de 100 reais nas contas que estão dentro da lista
def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

## também podemos realizar interrações por loop. Ex.:
for conta in contas:
   print("Informações antes de depositar 100: ",conta)


deposita_para_todas(contas)

## também podemos realizar interrações por loop. Ex.:
for conta in contas:
   print("Informações depois de depositar 100: ",conta)


## Agora caso em algum outro momento do nosso codigo adicionamos o numero da agencia dentro da lista de contas isso será um problema,
## caso formos realizar a chamado do metodo deposita. Ex.:
# contas.insert(0,76)

# deposita_para_todas(contas)

# for conta in contas:
#    print("Informações depois de depositar 100: ",conta)

## No trecho comentado acima ele dará erro, pois o elemento 76 dentro da lista contas não tem o metodo deposita
## Uma maneira de contarnar isso seria mudar o tipo da lista de contas para uma tupla. Porém isso significa que o metodo deposita precisará de alguns ajustes,
## pois um objeto do tipo Tupla, não permite alterar o valor dentro dele, uma vez instanciado não se pode mudar o conteudo dele. Mas podemos resolver esse problema



def deposita_para_todas_mod(conta): # Variação "funcional" (separando o comportados dos daos)
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo, novo_saldo)

## Declaração das Tuplas com informações de contas para atender o novo modelo de deposito
vitor = (76, 1000)
william = (76, 850)

## Criação de uma lista com Tuplas para realizar a chamadas do método de deposito
contas2 = [vitor, william]

for conta in contas2:
    conta = deposita_para_todas_mod(conta)
    print(conta)