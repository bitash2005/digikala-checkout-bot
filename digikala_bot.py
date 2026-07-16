from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

class Digikalabot:
    def __init__(self,driver:webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,15)
        
    def go_to_incredible_offers(self):
        all = (By.XPATH , "//a[@href='/incredible-offers/']")
        all_clik = self.wait.until(EC.element_to_be_clickable(all))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", all_clik)
        all_clik.click()
        self.wait.until(EC.url_contains("incredible-offers"))
        print("yes👌")
        
    def scroll_and_flter(self, discount=90):
        import random
        
        curren_p = 0
        last_p = self.driver.execute_script("return document.body.scrollHeight")
        visited_badges = set()
        
        while curren_p < last_p:
            self.driver.execute_script(f"window.scrollTo(0, {curren_p});")
            time.sleep(1) 
            
            discount_badges = self.driver.find_elements(By.CSS_SELECTOR, "[data-testid='price-discount-percent']")
            
            product_found_and_clicked = False
            for badge in discount_badges:
                try:
                    badge_id = badge.id
                    if badge_id in visited_badges:
                        continue
                    
                    visited_badges.add(badge_id)

                    discount_text = badge.text
                    discount_val = int(''.join(filter(str.isdigit, discount_text)))
                    
                    
                    if discount_val >= discount:
                        print(f" we find {discount_val}٪")
                        
                        
                        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", badge)
                        time.sleep(1)
                        
                        badge.click()
                        time.sleep(4) 
                        
                        self.add_to_cart()
                        
                        print("🔙 back to last page")
                        self.driver.back()
                        
                        product_found_and_clicked = True
                        break
                        
                except Exception as e:
                    continue
            
            
            if product_found_and_clicked:
                continue
            scroll_step = random.randint(350, 600)
            curren_p += scroll_step
            last_p = self.driver.execute_script("return document.body.scrollHeight")
            
        print("scann done")

def add_to_cart(self):
        
        try:
            
            cart_locator = (By.CSS_SELECTOR, "[data-cro-id='pdp-add-to-cart']")
            add_button = self.wait.until(EC.element_to_be_clickable(cart_locator))
            
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_button)
            time.sleep(1)
            add_button.click()
            print("product added sucsesfully")
            return True
        except Exception as e:
            print(f"error:{e}")
            return False        
    
        
            
    # def search_products(self , products):
    #     search_box = (By.NAME , "search-input")
    #     search_input = self.wait.until(EC.element_to_be_clickable(search_box))
    #     search_input.click()
    #     search_input.clear()
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(search_input).click().perform()
    #     time.sleep(0.5)
    #     actions.send_keys(products).perform()
    #     time.sleep(0.5)
    #     actions.send_keys(Keys.ENTER).perform()
    #     print("search secsussfully")
    #     time.sleep(5)