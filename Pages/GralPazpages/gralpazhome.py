from selenium.webdriver.common.by import By

class GralPazLocators():
    MAIL_ADDRESS = (By.CSS_SELECTOR, '.email1')
    
    class GralPazpages():
        
        def __init__(self, driver):
            self.driver = driver
            
        def get_mail_address(self):
            return self.driver.find_element(*GralPazLocators.MAIL_ADDRESS)