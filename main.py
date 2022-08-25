import json
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

BOTAO_PROXIMO =  "/html/body/div/div[2]/div[1]/nav/ul/li[contains(@class, 'next')]/a"
CITACAO = '/html/body/div/div[2]/div[1]/div'
FRASE = './span[1]'
AUTOR_NOME = './span[2]/small'
AUTOR_URL = './span[2]/a'
TAGS = './div/a'
TEMPO_ESPERA = 10 #segundos

class Navegador:
	def __init__(self):
		caminho_navegador='.//driver//chromedriver.exe'
		servc = webdriver.chrome.service.Service(caminho_navegador)
		opcoes = webdriver.ChromeOptions()
		opcoes.add_argument("start-maximized")
		opcoes.add_argument("disable-infobars")
		opcoes.add_argument("--disable-extensions")
		opcoes.add_argument('--no-sandbox')
		opcoes.add_argument('--disable-application-cache')
		opcoes.add_argument('--disable-gpu')
		opcoes.add_argument("--disable-dev-shm-usage")
		self.navegador = webdriver.Chrome(service=servc, options=opcoes)
	def coletar_citacoes(self):
		citacoes = []
		dicionario = {}
		print('INFO: Entrando no site...')
		ha_pagina = True
		self.navegador.get("http://quotes.toscrape.com/")
		while (ha_pagina):
			todas_citacoes = self.navegador.find_elements(By.XPATH, CITACAO)
			for citacao in todas_citacoes:
				citacoes.append({
					"quote":citacao.find_element(By.XPATH, FRASE).text[1:-1],
					"author":{
						"name":citacao.find_element(By.XPATH, AUTOR_NOME).text,
						"url":citacao.find_element(By.XPATH, AUTOR_URL).get_attribute('href')
					},
					"tags":[tag.text for tag in citacao.find_elements(By.XPATH, TAGS)]
				})
			try:
				espera = WebDriverWait(self.navegador, TEMPO_ESPERA).until(EC.element_to_be_clickable((By.XPATH, BOTAO_PROXIMO)))
			except TimeoutException:
				ha_pagina = False
			else:
				espera.click()
				WebDriverWait(self.navegador, TEMPO_ESPERA).until(EC.visibility_of_element_located(('xpath', CITACAO)))
		self.exportar_json(citacoes)

	def exportar_json(self, dicionario):
		print('INFO: Exportando arquivo .json...')
		with open("citacoes.json", "w") as arquivo:
			json.dump(dicionario, arquivo, indent=4)
if __name__ == '__main__':
	abrir = Navegador()
	abrir.coletar_citacoes()
	print('INFO: Fim do programa! Arquivo citacoes.json exportado!')