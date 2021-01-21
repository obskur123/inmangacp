from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidArgumentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pathlib import Path
import argparse, requests, logging, sys, os, re
from selenium import webdriver

FIREFOX = 'firefox'

CHROME = 'chrome'

logging.disable(logging.DEBUG)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def get_driver(browser_option):
    
    driver = None
    
    if browser_option == FIREFOX:
            
        options = webdriver.FirefoxOptions()

        options.headless = True

        driver = webdriver.Firefox(options=options)
        
    elif browser_option == CHROME:
        
        options = webdriver.ChromeOptions()
        
        options.headless = True
        
        driver = webdriver.Chrome(options=options)
        
            
    return driver

def initialize_parser():
    
    parser = argparse.ArgumentParser(description='descargar manga.')

    parser.add_argument('pos_navegador', help= 'Argumento de texto requerido.')

    parser.add_argument('pos_url', help= 'Argumento de texto requerido')

    parser.add_argument('--opt_ubicacion', help= 'Argumento de texto opcional.')

    return parser

def get_and_check_folder_name(driver : webdriver):
    
    folder_name = driver.find_element_by_xpath('/html/body/div/section/div/div/div[5]/h1').text
    
    checked_folder_name = re.sub('[^\w\-_\. ]', '_', folder_name)
    
    return checked_folder_name
    
def get_number_of_pages(driver : webdriver):
    
    logging.info('Obteniendo numero de paginas.')

    web_element_with_pages = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div/section/div/div/div[2]/div[1]/div/div/div[2]/div/select/option')))

    number_of_pages = len(web_element_with_pages)+1

    logging.info(f'Numero de paginas {number_of_pages}')

    return number_of_pages

def check_and_mk_dirs(folder_name, custom_path=None):
    
    home = str(Path.home())
    
    default_path = os.path.join(home, 'mangas')
    
    path = None
    
    if custom_path != None:
        
        path = os.path.join(custom_path, folder_name)
        
        os.mkdir(path)
        
    elif  os.path.exists(default_path):
        
        path = os.path.join(default_path, folder_name)
        
        os.mkdir(path)
            
        logging.info(f'Creando directorio: {folder_name}.')
            
    else:
            
        os.makedirs(os.path.join(default_path, folder_name))
        
        path = default_path
        
        logging.info(f'Creando directorio: {folder_name}.')
        
        
    return path

def get_url_image(driver : webdriver, page):

    img_web_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'/html/body/div/section/div/div/div[2]/div[2]/div[1]/a[{page}]/img')))

    return img_web_element.get_attribute('src')
    
def download_and_build_cap(driver : webdriver, number_of_pages, path):
        
    for page in range(1, number_of_pages):
        
        logging.info(f'Descargando pag num {page}.')

        r = requests.get(get_url_image(driver, page))
                                
        if r.status_code == 200:
            with open(os.path.join(path, f'page{page}.png'), 'wb') as f:
                for chunk in r:
                    f.write(chunk) 

        next_button = driver.find_element_by_xpath('/html/body/div/section/div/div/div[2]/div[1]/div/div/div[5]/div/button[2]').click()
        
    logging.info(f'Capitulo guardado en {path}.')


if __name__ == "__main__":
    
    args = initialize_parser().parse_args()

    driver = get_driver(args.pos_navegador)

    try:
        
        driver.get(args.pos_url)
        
        number_of_pages = get_number_of_pages(driver)

        folder_name = get_and_check_folder_name(driver)
        
        path = check_and_mk_dirs(folder_name, args.opt_ubicacion)
        
        download_and_build_cap(driver, number_of_pages, path)

            
    except InvalidArgumentException as e:
        logging.error(f'URL Invalida/No es una URL. - {e.msg}')
        driver.close()

    except  NoSuchElementException as e:
        logging.error(f'Incapaz de localizar elemento. - {e.msg}')
        driver.close()
        
    except TimeoutException as e:
        
        logging.error(f'Tiempo Expirado {e.msg}')
        driver.close()
        

    driver.close()

    
    


