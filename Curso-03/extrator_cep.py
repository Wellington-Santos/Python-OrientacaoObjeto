# Arquivo para validar a padronização do CEP dentro de uma string que contém endereço

# Regular Expression -- RegEx
import re

endereco = "Rua da Flores 72, apartamento 1062, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

# Formato CEP 5 digitos + hífen(opcional) + 3 digitos
# Obs.: Usar o simbolo '?' significa que aquela grupo de caracteres pode ou não aparece no padrão
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) # Match

if busca:
    cep = busca.group()
    print(cep)