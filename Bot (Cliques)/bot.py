from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

from time import sleep

links = [['https://sejasmm.com/', 0], ['https://brasilsmm.com/', 0]]

mainSearchPage = 'https://www.google.com'

driver = webdriver.Chrome (service=Service('./chromedriver.exe'))
driver.get(mainSearchPage)

aux = 0

for link in links:
    aux += 1
    driver.find_elements(By.XPATH, "//input[@class='gLFyf gsfi']")[0].send_keys('painel smm')
    driver.find_elements(By.XPATH, "//input[@class='gLFyf gsfi']")[0].send_keys(Keys.ENTER)

    if link[1] != 0:
        driver.find_elements(By.XPATH, f"//a[@aria-label='Page {link[1]}']")[0].send_keys(Keys.ENTER)

    driver.find_elements(By.XPATH, f"//a[@href='{link[0]}']")[0].send_keys(Keys.ENTER)

    if aux != len(links):
        driver.execute_script(f'''window.open("{mainSearchPage}","_blank");''')
        driver.switch_to.window(driver.window_handles[aux])

driver.execute_script(f'''window.open("http://192.168.1.1/index.html#login","_blank");''')

driver.switch_to.window(driver.window_handles[aux])

driver.find_elements(By.XPATH, f"//input[@id='txtPwd']")[0].send_keys('vivo')
driver.find_elements(By.XPATH, f"//input[@id='txtPwd']")[0].send_keys(Keys.ENTER)

sleep(1)
    
driver.get("http://192.168.1.1/index.html#others")

sleep(1)

driver.find_elements(By.XPATH, f"//input[@type='button']")[0].send_keys(Keys.ENTER)

driver.find_elements(By.XPATH, f"//input[@id='yesbtn']")[0].send_keys(Keys.ENTER)