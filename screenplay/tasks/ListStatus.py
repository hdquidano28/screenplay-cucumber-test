from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ListStatus:

 def perform_as(self, actor):
        wait = WebDriverWait(actor.driver, 10)
         # Click on the select dropdown
        dropdown = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]"))
        )
        dropdown.click()
        
        # Wait and click on Rejected option
        Rejected_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[text()='Rejected']"))
        )
        Rejected_option.click()