import requests as rq
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import sleep

def versao_atual():
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    sleep(5)

versao_atual()
