import random
from selenium import webdriver
import string



class rnd_registration(object):
    def __init__(self, URL):
        self.url = URL
        self.random_name()
        self.random_pwd()
        # self.random_mail_name()
        self.start_web_driver()

    def random_mail_name(self):
        """
        create random mail
        :return: full random mail
        """

        self._mail_name = random.choice(string.ascii_lowercase + string.digits)
        for _ in range(random.randrange(0, 15)):
            self._mail_name += str(random.choice(string.ascii_lowercase + string.digits + '_-'))
        self._hosting_name = '@'
        for _ in range(random.randrange(0, 9)):
            self._hosting_name += str(random.choice(string.ascii_lowercase + string.digits))
        self._hosting_loc = '.'
        for _ in range(random.randrange(2, 4)):
            self._hosting_loc += str(random.choice(string.ascii_lowercase))

        return self._mail_name + self._hosting_name + self._hosting_loc

    def random_name(self):
        self.rnd_name_reg = random.choice(string.ascii_lowercase + string.ascii_uppercase)
        for _ in range(random.randrange(0, 15)):
            self.rnd_name_reg += str(random.choice(string.ascii_lowercase + string.ascii_uppercase + '_'))
        return self.rnd_name_reg

    def random_pwd(self):
        self._rnd_pwd = random.choice(string.ascii_lowercase + string.ascii_uppercase
                                      + string.digits + '!@#$^&*()_+{}?><|')
        for _ in range(random.randrange(0, 15)):
            self._rnd_pwd += random.choice(string.ascii_lowercase + string.ascii_uppercase
                                           + string.digits + '!@#$^&*()_+{}?><|')
        return self._rnd_pwd







rnd_registration(URL='https://github.com')

# if __name__=='main':
#    main()
