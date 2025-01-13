import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class keepData:
     def perform_as(self, actor):
        wait = WebDriverWait(actor.driver, 20)
        # keepdataCheck = wait.until(
        #     EC.element_to_be_clickable((By.XPATH, "//*[text()='Recruitment']"))
        # )


        # keepdataCheck.click()

        saveBtn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@type='submit']"))
        )
        saveBtn.click()

        time.sleep(10)

     