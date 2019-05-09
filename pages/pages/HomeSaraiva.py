from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class SaraivaPage():

    def __init__(self, app):
        self.app = app
        # self.pagina('https://www.saraiva.com.br')

    def abrir_sitesaraiva(self):
        self.app.get('https://www.saraiva.com.br')

    def realiza_pesquisa(self):
        campo_pesquisa = self.app.find_element_by_id('q')
        campo_pesquisa.send_keys('Gestão da Emoção')
        botao_pesquisa = self.app.find_element_by_id('chaordic-search-button')
        sleep(2)
        botao_pesquisa.submit()
        #self.app.click("chaordic-search-button","id")
        

    def exibe_resultado(self):
        # assert self.app.title == "Gestão da emoção na Saraiva "
        # element = self.app.find_element_by_class_name('neemu-total-products-valor')
        # total = element.text
        element_2 = self.app.find_element_by_class_name('nm-searched-term')
        resultado = element_2
        # print(resultado.text)
        # print(total)
        assert resultado.text == 'Resultados para: Gestão da Emoção'
        #ssert element.text == "Resultados para: Gestão da emoção"
        #assert self.app.title == 'Gestão da emoção na Saraiva'