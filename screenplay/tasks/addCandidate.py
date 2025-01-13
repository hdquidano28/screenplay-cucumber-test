from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class addCandidate:

    def perform_as(self, actor):
        wait = WebDriverWait(actor.driver, 10)

        AddCandidate = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@class='oxd-button oxd-button--medium oxd-button--secondary']"))
        )
        AddCandidate.click()