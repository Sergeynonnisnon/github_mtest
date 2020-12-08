import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from settings import rnd_registration as rnd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

"""
тесты

2. создать тестовый гитхаб , на странице регистрации  авторизоваться 
3. из п.2 нажать на форгот пасс - отрицательная регистрация - проверить есть ли окно 
4. из 3 ввести верные значения - проверить получилось ли 
5. проверить существуют ли элементы вай гитхаб , експрор , прайсинг
6. зайти в прайсинг планс жми на джойн фри и заполнить данными (рандомными
7. нажать на эксплор гитхаб - топикс проверить что лейбл топик видно 
8 в строке поиска ввести вебдрайвер айо  - перейти на тайпскрипт перейти на первый и
 проверить что в юрлесть вебдрайвер айо
9. старт а фре трайал выбрать энтерпрайс клауд ввести дату вернуться назад и нажать на энтерпрайс сервер
заполнить данными и выбрать буттончики ввести что то в квестшонс нажать аксепт 
10. нажать на карьерс нажать на опен позишнс , спарсить все опен позишинс с выводом в консоль 



"""


class tests_suite_github(object):

    def __init__(self):
        self.rnd = rnd()


        self.test_case5_1()
        self.test_case5_2()

    def test_case1(self):

        """
         провести регистрацию через верхний сингин - проверить что перешли на след страницу и что существует
верифай йор акк
        :return: None
        """
        self.driver = webdriver.Firefox()
        self.driver.get('https://github.com')
        self.driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[2]/a[2]').click()

        self.username = self.driver.find_element_by_id('user_login')
        self.username.click()
        self.username.send_keys(self.rnd.random_name())

        self.mail = self.driver.find_element_by_id('user_email')
        self.mail.click()
        self.mail.send_keys(self.rnd.random_mail_name())

        self.paswd = self.driver.find_element_by_id('user_password')
        self.paswd.click()
        self.paswd.send_keys(self.rnd.random_pwd())
        """self.driver.find_element_by_xpath('/html/body/div[4]/main/div/div[1]/h1').click()
        action = ActionChains(driver=self.driver)
        elem = self.driver.find_element_by_xpath('/html/body/div[4]/main/div/div[2]/div/form/div[1]/h2')
        elem.click()
        action.key_up(Keys.ARROW_DOWN)
        action.perform()
        action.move_to_element(elem)"""
        if len(self.driver.find_elements(By.XPATH, '//*[@id="home"]')) > 0:
           print('exist')
        self.driver.quit()
        print ('test_case2 done')
    def test_case5_1(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://github.com')
        action = ActionChains(driver=self.driver)
        elem = self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/nav/ul/li[1]/details/summary')
        action.move_to_element(to_element=elem)
        action.perform()
        if len (self.driver.find_elements_by_xpath('/html/body/div[1]/header/div/div[2]/nav/ul/li[1]/details/div/a'))>0:
            print ("test_case2 done")
        else:
            print ('not find features')
        self.driver.quit()

    def test_case5_2(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://github.com')
        action = ActionChains(driver=self.driver)
        elem = self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/nav/ul/li[1]/details/summary')
        action.move_to_element(to_element=elem)
        action.perform()
        if len (self.driver.find_elements_by_xpath('/html/body/div[1]/header/div/div[2]/nav/ul/li[1]/details/div/ul[1]/li[1]/a'))>0:
            print ("test_case3 done")
        else:
            print ('not find code rewiew')
        self.driver.quit()




tests_suite_github()
