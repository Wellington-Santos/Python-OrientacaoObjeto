# Autor: Wellington Santos - 24/02/2023 00:41
# Começando a trabalhar com extrações de informações de strings e URLs

# url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
url = "bytebank.com/cambio?moedaOrigem=real"

print(url)

url_base = url[0:19]
url_parametros = url[20:36]

print(url_base)
print(url_parametros)
