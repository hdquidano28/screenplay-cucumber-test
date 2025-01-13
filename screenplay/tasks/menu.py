from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Menu:
    def perform_as(self, actor):
        wait = WebDriverWait(actor.driver, 20)
        recruitment_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[text()='Recruitment']"))
        )
      
        
        recruitment_button.click()
      
            