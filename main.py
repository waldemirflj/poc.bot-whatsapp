import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Whatsapp:
    def __init__(self):
        self.message = 'Opa... eh bot!'
        self.groups = ['Bot'] # Bot, Família, Família Santos
        self.sleep = 5

        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), 0, options)

    def sendMessageText(self):
        try:
            self.driver.get('https://web.whatsapp.com/')
            time.sleep(30) # hack

            for group in self.groups:
                group = self.driver.find_element_by_xpath(f'//span[@title="{group}"]')
                time.sleep(self.sleep) # hack
                group.click()

                textarea = self.driver.find_element_by_class_name('_3uMse')
                time.sleep(self.sleep) # hack
                textarea.click()
                textarea.send_keys(self.message)

                send = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
                time.sleep(self.sleep) # hack
                send.click()

                time.sleep(self.sleep) # hack

        except Exception as error:
            print('\n an exception occurred...')
            print('error: ', error)

        finally:
            self.driver.close()

    def sendMessageImage(self):
        try:
            self.driver.get('https://web.whatsapp.com/')
            time.sleep(30) # hack

            for group in self.groups:
                group = self.driver.find_element_by_xpath(f'//span[@title="{group}"]')
                time.sleep(self.sleep) # hack
                group.click()

                attachment = self.driver.find_element_by_xpath('//div[@title="Anexar"]')
                time.sleep(self.sleep) # hack
                attachment.click()

                image = self.driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                time.sleep(self.sleep) # hack
                image.send_keys('/home/waldemir/www/poc.bot-whatsapp/assets/unnamed.jpg')
                time.sleep(self.sleep) # hack

                send = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
                time.sleep(self.sleep) # hack
                send.click()

                time.sleep(self.sleep) # hack

        except Exception as error:
            print('\n an exception occurred...')
            print('error: ', error)

        finally:
            self.driver.close()

    def sendMessageDocument(self):
        try:
            self.driver.get('https://web.whatsapp.com/')
            time.sleep(30) # hack

            for group in self.groups:
                group = self.driver.find_element_by_xpath(f'//span[@title="{group}"]')
                time.sleep(self.sleep) # hack
                group.click()

                attachment = self.driver.find_element_by_xpath('//div[@title="Anexar"]')
                time.sleep(self.sleep) # hack
                attachment.click()

                image = self.driver.find_element_by_xpath('//input[@accept="*"]')
                time.sleep(self.sleep) # hack
                image.send_keys('/home/waldemir/www/poc.bot-whatsapp/assets/unnamed.pdf')
                time.sleep(self.sleep) # hack

                send = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
                time.sleep(self.sleep) # hack
                send.click()

                time.sleep(self.sleep) # hack

        except Exception as error:
            print('\n an exception occurred...')
            print('error: ', error)

        finally:
            self.driver.close()

wa = Whatsapp()
wa.sendMessageText()