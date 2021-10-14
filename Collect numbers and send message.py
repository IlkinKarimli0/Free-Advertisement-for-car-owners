#importing all necessary libraries

import os;
import random;
import time
from selenium.common.exceptions import TimeoutException
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

#cache w
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Revan\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\");
#options.add_argument('--profile-directory=Default')
options.add_argument("--start-maximized");


#starting driver
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)



class automessage:
    def __init__(self,message):
        self.bot = driver
        self.message = message
        self.source = "https://turbo.az/"
        self.platform = 'wa.me/'
        self.turbo()
        self.count = 0

    def turbo(self):
        #entering to site and some soft settings
        driver.get(self.source)
        driver.find_element_by_class_name('btn-full-search').click()
        driver.find_element_by_xpath('//*[@id="q_used"]/option[2]').click()
        driver.find_element_by_xpath('//*[@id="new_q"]/button').click()
        while True:
            #Declaring The Products
            ids = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "products")))

            element = WebDriverWait(ids[2], 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "products-i")))

            #salon filtiring
            
            salon = driver.find_elements_by_class_name("products-i.salon")
            
            main_window = driver.current_window_handle

            numbers = []

            #getting all numbers all numbers for page
            for ii in element:
                if(ii not in salon):
                    href = ii.find_element_by_class_name('products-i__link').get_attribute('href')
                    numbers.append(self.get_number(href))

            #Cleareance

            texted_numbers_strip = []

            # reading users from file
            if (os.path.isfile('users.txt')):
                with open('users.txt', 'r') as f:
                    texted_numbers = f.readlines()
                for texted_number in texted_numbers:
                    texted_numbers_strip.append(texted_number.strip())
                textable_numbers = []
                for number in numbers:
                    if not number in texted_numbers_strip:
                        textable_numbers.append(number)
                numbers = textable_numbers


            #sending messages to numbers
            for number in numbers:
                self.wa_send(number)
            driver.find_element_by_class_name('next').click()

        

    def get_number(self,href):
        driver.execute_script("window.open('');")
  
        #Opening href in new window
        driver.switch_to.window(driver.window_handles[1])
        driver.get(href)
        
        number = driver.find_element_by_class_name('phone').get_attribute('href')
        #closing window
        driver.close()    
        #going back
        driver.switch_to.window(driver.window_handles[0])
        
        return number
    
    def get_ready_numbers(self,unready_numbers): 
        pass

    def wa_send(self,st):
        url = 'https://web.whatsapp.com/send?phone=%2B994'+st[6:8]+st[10:13]+st[14:16]+st[17:19]+'&text&app_absent=0'
        #url = 'https://wa.me/+994'+st[6:8]+st[10:13]+st[14:16]+st[17:19]
        driver.execute_script("window.open('');")
        print(url)
        #Opening href in new window
        driver.switch_to.window(driver.window_handles[1])
        driver.get(url)
        time.sleep(10)
        try:
            undefined = driver.find_element_by_class_name('_2Nr6U')
            if(undefined):
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                print('Number is not defined')
                with open('users.txt', 'a+') as f:
                    f.write(st+'\n')
        except NoSuchElementException:
            checking = True
            count = 5
            while checking and count>=0:
                try:
                    inbox_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')))
                    if(inbox_element):
                        checking = False

                    #sending
                    inbox_element.send_keys(Keys.CONTROL + 'v')
                    time.sleep(1)
                    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[2]/div[2]/div/div/span').click()
                    time.sleep(3)
                    print('Have sent \n')
                    with open('users.txt', 'a+') as f:
                        f.write(st + '\n')
                    print(1)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    
                    
                except TimeoutException:
                    count=count-1
                    checking = False
                    
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    driver.execute_script("window.open('');")
                    driver.switch_to.window(driver.window_handles[1])
                    driver.get(url)
                    time.sleep(5)
            if count == 0:
                driver.close()
                driver.switch_to.window(driver.window_handles[0])






        

automessage('')

