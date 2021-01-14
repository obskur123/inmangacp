from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
import logging
import time
import sys
import os



logging.disable(logging.DEBUG)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

options = Options()

options.headless = True

driver = webdriver.Firefox(options=options)

try:
    
    driver.get(sys.argv[1])
    
    logging.info('Obteniendo numero de paginas.')

    web_element_with_pages = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div/section/div/div/div[2]/div[1]/div/div/div[2]/div/select/option')))

    number_of_pages = len(web_element_with_pages)

    logging.info(f'Numero de paginas: {number_of_pages}')

    requests_array = []

    folder_name = driver.find_element_by_xpath('/html/body/div/section/div/div/div[5]/h1').text
    
    for i in range(1, number_of_pages+1):
    
        logging.info(f'Descargando pag num {i}.')
        
        img_web_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'/html/body/div/section/div/div/div[2]/div[2]/div[1]/a[{i}]/img')))

        url_image = img_web_element.get_attribute('src')

        r = requests.get(url_image)

        requests_array.append(r)
        
        next_button = driver.find_element_by_xpath('/html/body/div/section/div/div/div[2]/div[1]/div/div/div[5]/div/button[2]').click()
        
    
    
except InvalidArgumentException as e:
    logging.error(f'URL Invalida/No es una URL. - {e.msg}')
    driver.close()
    sys.exit()

except  NoSuchElementException as e:
    logging.error(f'Incapaz de localizar elemento. - {e.msg}')
    driver.close()
    sys.exit('Solo acepto URL\'s de capitulos de inmanga.')




os.mkdir(f'{os.getcwd()}\\{folder_name}')
logging.info(f'Creando directorio: {folder_name}.')
    
page = 1
for request in requests_array:
    logging.info(f'Construyendo pag num {page}')
    if request.status_code is 200:
        with open(f'{folder_name}\\page{page}.png', 'wb') as f:
            for chunk in request:
                f.write(chunk) 
    page+=1
    
driver.close()

    
    


