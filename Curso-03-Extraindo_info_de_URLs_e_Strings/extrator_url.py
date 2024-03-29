import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.limpa_url(url)
        self.valida_url()

# Métodos especiais do Python para permitir que ser possivel realizar print, len e comparação do conteudo da classe
    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return self.url
    
    def __eq__(self, other):
        return self.url == other.url

    def limpa_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""
        
# Refatoração do método, além de validar se e URL esta vazia, se ela está em um formato padronizado de URL
# também esta sendo utilizado método 'match' da propriedade re (Regular Expression), verificar se a string como um todo igual ao padrão  
    def valida_url(self):        
        if not self.url:
            raise ValueError("A URL está vazia")
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é válida")

        # print("A URL é válida")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):        
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)

        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor


# extrator_url = ExtratorURL(None)
url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

extrator_url = ExtratorURL(url)

extrator_url2 = ExtratorURL(url)

print("O tamanho da URL: ", len(extrator_url))
print(extrator_url)

print(extrator_url == extrator_url2)

# valor_quantidade = extrator_url.get_valor_parametro("quantidade")
# print(valor_quantidade)