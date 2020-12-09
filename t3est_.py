from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import rnd_registration as rnd
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

        self.test_case1()
        #self.test_case5_1()
        #self.test_case5_2()

    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://github.com')

    def test_case1(self):

        """
         провести регистрацию через верхний сингин - проверить что перешли на след страницу и что существует
верифай йор акк
        :return: None
        """
        self.setup_method()
        #print (self.driver.window_handles())
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

        self.driver.implicitly_wait(5)
        self.varification_test = len(self.driver.find_elements(By.XPATH,
                                                              "//a[@id=\"home_children_button\"]"))
        self.btn_test = len(self.driver.find_elements(By.XPATH,
                                                      "/html/body/div[4]/main/div/div[2]/div/form/div[2]"))
        assert self.varification_test == 1,"Error verification dont exist"
        assert self.btn_test == 1, "Error Button registration dont exist"
        self.driver.quit()


    def test_case5_1(self):
        self.setup_method()
        action = ActionChains(driver=self.driver)
        elem = self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]'
                                                 '/nav/ul/li[1]/details/summary')
        action.move_to_element(to_element=elem)
        action.perform()
        assert len(self.driver.find_elements_by_xpath
                   ('/html/body/div[1]/header/div/div[2]/nav/ul/li[1]/details/div/a')) == 1, 'not find features'
        print('test_case5_1 done')
        self.driver.quit()

    def test_case5_2(self):
        self.setup_method()
        action = ActionChains(driver=self.driver)
        elem = self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/nav'
                                                 '/ul/li[1]/details/summary')
        action.move_to_element(to_element=elem)
        action.perform()
        if len(self.driver.find_elements_by_xpath(
                '/html/body/div[1]/header/div/div[2]/nav/ul/li[1]/detail'
                's/div/ul[1]/li[1]/a')) > 0:
            print("test_case3 done")
        else:
            print('not find code rewiew')
        self.driver.quit()


tests_suite_github()
