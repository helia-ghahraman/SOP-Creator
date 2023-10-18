# from lib2to3.pgen2 import driver
#
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from time import sleep
#
# chromedriver_path = ".//chromedriver.exe"
# options = webdriver.ChromeOptions()
# options.add_argument("user-data-dir=C:\\Users\\USER\\AppData\\Local\\Google\\Chrome\\User Data")
# prefs = {"profile.managed_default_content_settings.images": 2}
# options.page_load_strategy = 'normal'
# page = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=options)
#
#
# if __name__ == '__main__':
#     page.get("https://smodin.io/writer")
#     sleep(3)
#     box = page.find_element("xpath",'//*[@id="__next"]/div[3]/div/div/div/div[2]/div/div[1]/div[3]/div[1]/div/p[2]')
#     box.click()
#     sleep(3)
#     input = page.find_element("xpath",'//*[@id="__next"]/div[3]/div/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/input')
#     input.send_keys("Stanford")
#     sleep(2)
#     input.send_keys(Keys.ENTER)
#     sleep(60)
#
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

chromedriver_path = ".//chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\USER\\AppData\\Local\\Google\\Chrome\\User Data")
prefs = {"profile.managed_default_content_settings.images": 2}
options.page_load_strategy = 'normal'

try:
    page = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=options)
    page.get("https://smodin.io/writer")
    sleep(3)

    box = WebDriverWait(page, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[3]/div/div/div/div[2]/div/div[1]/div[3]/div[1]/div/p[2]')))
    box.click()
    sleep(3)

    input = WebDriverWait(page, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[3]/div/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/input')))
    input.send_keys("Stanford")
    sleep(2)
    input.send_keys(Keys.ENTER)
    sleep(60)

except TimeoutException:
    print("Timeout occurred while waiting for element to be found")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    page.quit()


