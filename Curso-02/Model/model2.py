class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas ... ')
    
    def mostrar_tarefas(self):
        print('Fez muita coisa ... ')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer ... ')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alureta')

    def busca_perguntas_sem_respostas(self):
        print('Mostrando perguntas não resposndidas do fórum')

class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum, Hipster):
    pass

# teste = Junior()
# teste.mostrar_tarefas

# wellington = Pleno()
# wellington.mostrar_tarefas()

teste = Senior('Wellington')
print(teste)