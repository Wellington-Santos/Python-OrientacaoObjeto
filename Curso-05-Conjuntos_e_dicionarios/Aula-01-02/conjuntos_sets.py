# Massa de dados para ser estudar os conjuntos e sets
usuarios_data_science = [15,23,43,56]
usuarios_machine_learning = [13,23,56,42]

# iremos unir as duas listas para sets
alunos = usuarios_data_science.copy()
alunos.extend(usuarios_machine_learning)

print(alunos)

# Ao executar perceberá que tem numeros de alunos repetidos e não queremos isso
# para isso iremos teremos que tratar as informações, mudando para conjunto 

# podemos setar as listas para set, usando o set ele muda para conjunto e com isso 
# remove os valores repetidos
set_alunos= set(alunos)
print(set_alunos)

# Agora caso queira ter um objeto ja como conjunto e queira unir ele fazemos dessa maneira
usuarios_data_science_ = {15,23,43,56}
usuarios_machine_learning_ = {13,23,56,42}

turma = usuarios_data_science_ | usuarios_machine_learning_
print(turma)


# Alunos que fizeram os dois cursos
alunos_data_science_e_machine_learning = usuarios_data_science_ & usuarios_machine_learning_

# Alunos que fizeram apenas Data Science
alunos_data_science = usuarios_data_science_ - usuarios_machine_learning_

print(alunos_data_science_e_machine_learning)
print(alunos_data_science)

# Conjunto ele é iteravel, podemos adicionar itens nele, porém podemos congelar ele também, impedindo de add itens

# Add itens no conjunto
alunos_data_science.add(135)

# Travando um conjunto
Alunos_travados = frozenset(alunos_data_science)