from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class listVacancy:

    def perform_as(self, actor):
        wait = WebDriverWait(actor.driver, 20)
         # Click on the select dropdown
        dropdown = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'-- Select --')]"))
        )
        dropdown.click()
        
        # Wait and click on Senior QA Lead option
        SeniorQALead_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[text()='Senior QA Lead']"))
        )
        SeniorQALead_option.click()