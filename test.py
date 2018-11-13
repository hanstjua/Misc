from bs4 import BeautifulSoup as bs
import requests as rq
import webbrowser as wbb
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import random

vals = {'emailOrPhone': 'koawekoroszss@gmail.com',
 'fullName': 'Korokor Su',
 'password': 'L0ckhe@d',
 'username': 'kokorozxcs'}

site = rq.get('http://www.instagram.com',params=vals)

soup = bs(site.content,'html.parser')

print(soup.prettify())

driver = wd.Safari()

driver.get('http://www.instagram.com')

eml = driver.find_element_by_name('emailOrPhone')
full = driver.find_element_by_name('fullName')
pwd = driver.find_element_by_name('password')
usr = driver.find_element_by_name('username')

idx = str(random.randInt(1,10000))

eml.send_keys('koawekoroszss@gmail.com')
full.send_keys('Korokor Su')
pwd.send_keys('L0ckhe@d')
usr.send_keys('kokorozxcs'+idx)

submit = driver.find_element_by_class('_qv64e _gexxb _4tgw8 _njrw0')

submit.click()

#logged in for the first time

