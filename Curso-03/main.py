# Autor: Wellington Santos - 24/02/2023 00:41
# Começando a trabalhar com extrações de informações de strings e URLs

url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

# Separa a URL base e os parametros
indice_interrogacao = url.find('?')
url_base = url[: indice_interrogacao]
url_parametros = url[indice_interrogacao + 1 :]

# Busca o valor de um parâmetro
# parametro_busca = 'moedaOrigem'
parametro_busca = 'moedaDestino'

indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1

indice_e_comercial = url_parametros.find('&', indice_valor)

if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]


print(url_parametros)
print(valor)
