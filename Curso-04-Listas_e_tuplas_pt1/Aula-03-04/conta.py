from abc import ABCMeta, abstractmethod
from functools import total_ordering
from operator import attrgetter

class Conta(metaclass=ABCMeta):

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo: {} Saldo: {}<<]".format(self._codigo, self._saldo)
    
    @abstractmethod
    def pass_o_mes(self):
        pass

class ContaCorrente(Conta):
    
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    pass

@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False

        return self._codigo == outro._codigo
    
    def __lt__(self, outro):
        if self._saldo != outro._saldo: 
            return self._saldo < outro._saldo
        
        return self._codigo < outro._codigo
    
    def __str__(self):
        return "[>>Codigo: {} Saldo: {}<<]".format(self._codigo, self._saldo)

# conta16 = ContaCorrente(16)
# conta16.deposita(100)

# conta17 = ContaPoupanca(17)
# conta17.deposita(1000)
# conta17.passa_o_mes()

# conta1 = ContaSalario(1)
# conta2 = ContaSalario(1)

# contas = [conta16, conta17]

# for conta in contas:
#     conta.passa_o_mes()
#     print(conta)

# print (conta1 == conta2)

conta_do_guilherme = ContaSalario(37)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(25)
conta_do_paulo.deposita(750)

def extrai_saldo(conta):
    return conta._saldo

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

# for conta in sorted(contas, key=attrgetter("_saldo")):
#     print(conta)

for conta in sorted(contas):
    print(conta)

print("\n")

for conta in sorted(contas, reverse=True):
    print(conta)

print(conta_do_guilherme < conta_da_daniela)