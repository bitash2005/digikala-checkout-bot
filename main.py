from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import sys
import traceback
from digikala_bot import Digikalabot

if '__file__' in locals():
    c_directory = os.path.dirname(os.path.abspath(__file__))
else:
    c_directory = os.getcwd()

local_driver_path = os.path.join(c_directory, "chromedriver.exe")
chrom_servis = Service(executable_path=local_driver_path)

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=chrom_servis, options=chrome_options)

try:
    print("Opening Digikala...")
    driver.get("https://www.digikala.com/")
    driver.maximize_window()
    
    bot = Digikalabot(driver)
    
    print("Navigating to Incredible Offers...")
    bot.go_to_incredible_offers()
    print("Type the desired discount percentage amount :")
    
    n = int(input())

    
    print("Starting product scan and filtering...")
    bot.scroll_and_flter(discount=n)
    
    print("Proceeding to checkout...")
    bot.go_to_checkout()
    bot.compelite_shopping()
    bot.login_user()
    bot.admit_by_code()
    
    
except Exception as e:
    print("An error occurred during execution:")
    traceback.print_exc()