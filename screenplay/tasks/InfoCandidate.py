from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InfoCandidate:

     def __init__(self, firstName,  Middle_Name , last_name , email, phone, Keywords, notes ):
      
        self.firstName = firstName
        self.Middle_Name = Middle_Name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.Keywords = Keywords
        self.notes = notes
        

     def perform_as(self, actor):
        wait = WebDriverWait(actor.driver, 10)

        name = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='firstName']"))
        )
        Middle_Name_field  = actor.driver.find_element(By.XPATH, "//input[@name='middleName']")
        last_name_field  = actor.driver.find_element(By.XPATH, "//input[@name='lastName']")
        email_field = actor.driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/input[1]")
        phone_field = actor.driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/div[2]/input[1]")
        Keywords_field = actor.driver.find_element(By.XPATH, "//input[@placeholder='Enter comma seperated words...']")
        note_field = actor.driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[6]/div[1]/div[1]/div[1]/div[2]/textarea[1]")
        
        

        name.send_keys(self.firstName)
        Middle_Name_field.send_keys(self.Middle_Name)
        last_name_field.send_keys(self.last_name)
        email_field.send_keys(self.email)
        phone_field.send_keys(self.phone)
        Keywords_field.send_keys(self.Keywords)
        note_field.send_keys(self.notes)
       



