from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import random
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

def web(input):

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://www.mcdvoice.com/?AspxAutoDetectCookieSupport=1")
    elem = driver.find_element_by_id("CN1")
    elem.send_keys(input[0])
    elem = driver.find_element_by_id("CN2")
    elem.send_keys(input[1])
    elem = driver.find_element_by_id("CN3")
    elem.send_keys(input[2])
    elem = driver.find_element_by_id("CN4")
    elem.send_keys(input[3])
    elem = driver.find_element_by_id("CN5")
    elem.send_keys(input[4])
    elem = driver.find_element_by_id("CN6")
    elem.send_keys(input[5])

    driver.find_element_by_id("NextButton").click()

    elemArr1 = driver.find_elements_by_class_name("radioButtonHolder")
    elemArr1[random.randint(0,2)].click()

    driver.find_element_by_id("NextButton").click()

    elemArr2 = driver.find_elements_by_class_name("radioBranded")
    elemArr2[random.randint(0,4)].click()

    elemArr2 = driver.find_elements_by_class_name("radioBranded")
    elemArr2[random.randint(0,4)].click()

    driver.find_element_by_id("NextButton").click()

    while True:
        try:
            driver.find_element_by_id("NextButton").click()
        except:
            break

    return driver.find_element_by_class_name('ValCode').text

userin = ['25666', '13531', '03019', '18348', '00034', '7']
print(web(userin))
