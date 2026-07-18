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
        print("yes")
        
    def scroll_and_flter(self, discount =90 ):
        import random
        
        curren_p = 0
        last_p = self.driver.execute_script("return document.body.scrollHeight")
        visited_products = set()
        count = 0
        while curren_p < last_p:
            self.driver.execute_script(f"window.scrollTo(0, {curren_p});")
            
            time.sleep(0.5) 
            
            discount_badges = self.driver.find_elements(By.CSS_SELECTOR, "[data-testid='price-discount-percent']")
            
            product_found_and_clicked = False
            for badge in discount_badges:
                try:
                    product_link_element = badge.find_element(By.XPATH, "./ancestor::a")
                    product_url = product_link_element.get_attribute("href").split("?")[0]
                    
                    if product_url in visited_products:
                        continue
                    
                    visited_products.add(product_url)

                    discount_text = badge.text
                    discount_val = int(''.join(filter(str.isdigit, discount_text)))
                    
                    if discount_val >= discount:
                        print(f" we find {discount_val}٪")
                        count+=1
                        
                        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", badge)
                        time.sleep(1)
                        
                        badge.click()
                        time.sleep(4) 
                        
                        self.add_to_cart()
                        
                        print(" back to last page")
                        self.driver.back()
                        time.sleep(3.5) 
                        
                        product_found_and_clicked = True
                        break
                        
                except Exception as e:
                    continue
            
            if product_found_and_clicked:
                continue
                
            
            scroll_step = random.randint(250, 450)
            curren_p += scroll_step
            last_p = self.driver.execute_script("return document.body.scrollHeight")
            
        print("scann done")
        
        
        if(count==0):
            print("nothing found")
            self.driver.quit()
            return
            
            
        
        print(" back to last page")
        self.driver.back()
        time.sleep(3.5)
    
    def go_to_checkout(self):
        try:
            print("moving to shopping cart icon")
            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(1)
            
            cart_icon_element = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-cro-id='header-cart']"))
            )
            
            action = ActionChains(self.driver)
            action.move_to_element(cart_icon_element).perform()
            print("hovered yes")
            time.sleep(2)
            
            cheked_btn_loc = (By.XPATH , "//div[contains(text(), 'ثبت سفارش') or contains(., 'ثبت سفارش')]/ancestor::a | //div[contains(text(), 'ثبت سفارش')]")
            cheked_btn = self.wait.until(EC.element_to_be_clickable(cheked_btn_loc))
            self.driver.execute_script("arguments[0].click();", cheked_btn)
            print("Clicked on button successfully!")
            time.sleep(3)
            return True
        except Exception as e:
            print(f"Error in go_to_checkout: {e}")
            return False

            
    def add_to_cart(self):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        import time

        wait = WebDriverWait(self.driver, 15)
        
        print("eaiting for ad to cart button")
        
        locators = [
            (By.XPATH, "//div[contains(text(), 'افزودن به سبد خرید')]/ancestor::button"),
            (By.XPATH, "//button[contains(., 'افزودن به سبد خرید')]"),
            (By.CSS_SELECTOR, "[data-testid='add-to-cart']")
        ]
        
        add_button = None
        for locator in locators:
            try:
                add_button = wait.until(EC.presence_of_element_located(locator))
                if add_button:
                    print(f" find it Successfully {locator}")
                    break
            except:
                continue
                
        if not add_button:
            print("we cant find ad to cart Button")
            return False

        try:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_button)
            time.sleep(0.5)
            
            self.driver.execute_script("arguments[0].click();", add_button)
            print("  product add succussfully")
            return True
        except Exception as e:
            print(f"ERROR {e}")
            return False
        
    def compelite_shopping(self):
        try:
            print("waiting for loading page")
            shopping_loc = (By.CSS_SELECTOR,"a[href*='/checkout/shipping/']")
            shopping_btn = self.wait.until(EC.element_to_be_clickable(shopping_loc))
            shopping_btn.click()
            
        except:
            print("error")
            
    def login_user(self):
        try:
            print("\n" + "="*40)
            print("enter your phon_number or email please :")
            n_e = input()
            user_name = self.wait.until(EC.presence_of_element_located((By.ID, "username")))
            user_name.click()
            user_name.clear()
            user_name.send_keys(n_e)
            
            login_btn = self.wait.until(EC.element_to_be_clickable((By.ID,"dk-login")))
            login_btn.click()
        except Exception as e:
            print(f"Error in login_user: {e}")
            return False
    def admit_by_code(self):
        print("\n" + "="*40)
        print("please enter the code that Digikala send to you:")
        code = input()
        input_code = self.wait.until(EC.presence_of_element_located((By.ID ,"code")))
        input_code.click()
        input_code.clear()
        input_code.send_keys(code)
        admit_btn = self.wait.until(EC.element_to_be_clickable((By.ID ,"dk-form-buttons")))
        admit_btn.click()
     