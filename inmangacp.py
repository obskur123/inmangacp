from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from tqdm import tqdm
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

    folder_name = driver.find_element_by_xpath('/html/body/div/section/div/div/div[5]/h1').text
    
    if ':' in folder_name:
        
        folder_name = folder_name.replace(':','-')
        
                
    if not os.path.exists('.\\Mangas'):
                
        os.mkdir('.\\Mangas')
            
        os.mkdir(f'.\\Mangas\\{folder_name}')
            
        logging.info(f'Creando directorio: {folder_name}.')
            
    else:
            
        os.mkdir(f'.\\Mangas\\{folder_name}')
        logging.info(f'Creando directorio: {folder_name}.')
    
    
    for i in range(1, number_of_pages+1):
        
        logging.info(f'Descargando pag num {i}.')
        
        img_web_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'/html/body/div/section/div/div/div[2]/div[2]/div[1]/a[{i}]/img')))

        url_image = img_web_element.get_attribute('src')

        r = requests.get(url_image)
        
        total_size_in_bytes = int(r.headers.get('content-length', 0))
        
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
                
        if r.status_code is 200:
            with open(f'.\\Mangas\\{folder_name}\\page{i}.png', 'wb') as f:
                for chunk in r.iter_content(1024):
                    progress_bar.update(len(chunk))
                    f.write(chunk) 
            progress_bar.close()

        next_button = driver.find_element_by_xpath('/html/body/div/section/div/div/div[2]/div[1]/div/div/div[5]/div/button[2]').click()
        
except InvalidArgumentException as e:
    logging.error(f'URL Invalida/No es una URL. - {e.msg}')
    driver.close()
    sys.exit()

except  NoSuchElementException as e:
    logging.error(f'Incapaz de localizar elemento. - {e.msg}')
    driver.close()
    sys.exit('Solo acepto URL\'s de capitulos de inmanga.')
    
except TimeoutException as e:
    
    logging.error(f'Tiempo Expirado {e.msg}')
    driver.close()
    sys.exit()

logging.info(f'Capitulo guardado en .\\Mangas\\{folder_name}.')
driver.close()

    
    


