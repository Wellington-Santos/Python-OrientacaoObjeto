class Conta:

    # Inicialização da classe Conta, nela teremos alguns metodos básicos para realizar algumas ações simples com conceitos de Orientações a Objetos

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do Titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if(self.__disponivel_saque(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def __disponivel_saque(self, valor):
        valor_disponivel = self.__saldo + self.limite
        return valor <= valor_disponivel

    # Adição de um metodo para realizar transferências entre contas instânciadas em memória, sem redundância de código e o mais simples possível
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    # Adição dos metodos Get e Set para realizar consultas simples e alteração no limite da conta
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    # Usando os termos Property e Setter nos metódos de limites pois e mais facil e compreensivel de entender o código e evita de re-criar código desnecessário
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def saldo(self, valor):
        self.__limite = valor

    @staticmethod
    def codigo_banco(self):
        return "001"