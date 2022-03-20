import os
import random
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


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\"UR_USERNAME"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\");
#options.add_argument('--profile-directory=Default')
options.add_argument("--start-maximized");


#starting driver
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)



driver.get("https://turbo.az/")


#numbers
texted_numbers_strip = []

# reading numbers list
if (os.path.isfile('turbo.az.txt')):
    with open('turbo.az.txt', 'r') as f:
        texted_numbers = f.readlines()
    for texted_number in texted_numbers:
        texted_numbers_strip.append(texted_number.strip())
    numbers = texted_numbers_strip

texted_numbers_strip = []

print(len(numbers))

# reading if we sent or not
if (os.path.isfile('sent_numbers.txt')):
    with open('sent_numbers.txt', 'r') as f:
        texted_numbers = f.readlines()
    for texted_number in texted_numbers:
        texted_numbers_strip.append(texted_number.strip())
    print(len(texted_numbers_strip))
    textable_numbers = []
    for number in numbers:
        if not number in texted_numbers_strip:
            textable_numbers.append(number)
    numbers = textable_numbers


print(len(numbers))
def wa(st):
    url = 'https://web.whatsapp.com/send?phone=%2B'+st+'&text&app_absent=0'

    # url = 'https://wa.me/+994'+st[6:8]+st[10:13]+st[14:16]+st[17:19]
    driver.execute_script("window.open('');")
    print(url)
    # Opening href in new window
    driver.switch_to.window(driver.window_handles[1])
    driver.get(url)
    time.sleep(10)
    try:
        undefined = driver.find_element_by_class_name('_2Nr6U')
        if (undefined):
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            print('Number is not defined')
            with open('sent_numbers.txt', 'a+') as f:
                f.write(st + '\n')
    except NoSuchElementException:
        checking = True
        count = 5
        while checking and count >= 0:
            try:
                inbox_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')))
                if (inbox_element):
                    checking = False

                # sending
                inbox_element.send_keys(Keys.CONTROL + 'v')
                time.sleep(1)
                text_area =  driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]')

                text_area.send_keys('Salam, Ən ucuz Avtomobil ehtiyyat hissələri bizdə. Bazar qiymətinin 50%-80% faizinə Avtomobil ehtiyyat hissələri.         Hörmətlə:  FN auto parts')
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[2]/div[2]/div/div/span').click()
                #inbox_element.send_keys(Keys.ENTER)
                #driver.find_element_by_class_name('_1w1m1').click()
                time.sleep(3)
                print('Have sent \n')
                with open('sent_numbers.txt', 'a+') as f:
                    f.write(st + '\n')
                print(1)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])


            except TimeoutException:
                count = count - 1
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

for number in numbers:
    wa(number)






