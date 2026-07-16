from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time
from digikala_bot import Digikalabot




c_directory= os.path.dirname(os.path.abspath(__file__))
local_driver_path = os.path.join( c_directory, "chromedriver.exe")
chrom_servis = Service(executable_path=local_driver_path)
driver = webdriver.Chrome(service=chrom_servis)


try:
    driver.get("https://www.digikala.com/")
    driver.maximize_window()
    bot = Digikalabot(driver)
    bot.go_to_incredible_offers()
    bot.scroll_and_flter()
    
    
    
    
    
    
except Exception as e :
    print("error")
    import traceback
    traceback.print_exc()
    
finally:
    time.sleep(3)
    driver.quit()