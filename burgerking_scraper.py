from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

def web(input, input2):

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://www.mybkexperience.com")
    elem = driver.find_element_by_id("Initial_StoreID")
    elem.send_keys(input[0])

    driver.find_element_by_id("NextButton").click()

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "CN1"))
        )
    finally:
        elem2 = driver.find_element_by_id("CN1")
        elem2.send_keys(input2[0])
        elem2 = driver.find_element_by_id("CN2")
        elem2.send_keys(input2[1])
        elem2 = driver.find_element_by_id("CN3")
        elem2.send_keys(input2[2])
        elem2 = driver.find_element_by_id("CN4")
        elem2.send_keys(input2[3])

        driver.find_element_by_id("NextButton").click()

#Next button Loop
    while True:
        try:
            driver.find_element_by_id("NextButton").click()
        except:
            break

    return driver.find_element_by_class_name('ValCode').text
    
userin = ['6975']
userin2 = ['10149', '28268', '01652', '206975']
print(web(userin, userin2))
