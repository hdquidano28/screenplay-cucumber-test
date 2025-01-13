from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InfoInterview:

     def __init__(self, name,  interviewer_field , date_field):
      
        self.name = name
        self.interviewer_field = interviewer_field
        self.date_field = date_field

        

     def perform_as(self, actor):
        wait = WebDriverWait(actor.driver, 10)

        name = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input"))
        )
        interviewer_field  = actor.driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']")
        date_field  = actor.driver.find_element(By.XPATH, "//input[@placeholder='yyyy-dd-mm']")
    
        

        name.send_keys(self.name)
        interviewer_field.send_keys(self.interviewer_field)
        date_field.send_keys(self.date_field)




