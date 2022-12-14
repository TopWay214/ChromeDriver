import requests as rq

def ultima_versao():
    url = ("https://chromedriver.chromium.org/downloads")
    site = rq.get(url)
    conteudo_byt = site.content
    conteudo = str(conteudo_byt)
    filtro = conteudo.split('https://chromedriver.storage.googleapis.com/index.html?path=')
    versao = filtro[1][0:13]
    print(versao)

ultima_versao()
