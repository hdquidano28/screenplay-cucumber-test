from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def perform_as(self, actor):
        wait = WebDriverWait(actor.driver, 10)
        
        username_field = wait.until(
         EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
        )
        password_field = actor.driver.find_element(By.XPATH, "//input[@name='password']")
        login_button = actor.driver.find_element(By.XPATH, "//button[@type='submit']")

        username_field.send_keys(self.username)
        password_field.send_keys(self.password)
        login_button.click()