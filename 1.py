import time
import os
from selenium import webdriver

if not os.path.exists('folder'):
    os.mkdir('folder')

driver = webdriver.Firefox()

my_login = 'логин в госуслуги'
my_password = 'пароль в госуслуги'

driver.get('https://www.gosuslugi.ru/')
driver.maximize_window()
time.sleep(3)
register = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div/div[3]/div/div/a').click()
time.sleep(1)
input_login = driver.find_element_by_xpath('//*[@id="login"]')
input_password = driver.find_element_by_xpath('//*[@id="password"]')
submit = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[1]/form/div[1]/div/div[4]/div[2]/button/span')
input_login.send_keys(my_login)
time.sleep(1)
input_password.send_keys(my_password)
time.sleep(1)
submit.click()
time.sleep(3)
my_doc = driver.find_element_by_xpath('/html/body/lk-root/main/div/lib-tabs/nav/div/ul/li[3]/a/span')
my_doc.click()
time.sleep(1)
div_info = driver.find_element_by_class_name('content')

if not os.path.exists('folder/text.txt'):
    f = open('folder/text.txt', 'w')
    for i in div_info.text:
        f.write(i)

driver.close()
