import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HandleApplicationStage:
    def perform_as(self, actor):
        wait = WebDriverWait(actor.driver, 10)
        
        # Esperar a que aparezca el formulario
        form = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'oxd-form')]"))
        )
        
        # Localizar el botón "Shortlist" dentro del formulario
        shortlist_btn = form.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div[1]/form/div[2]/div[2]/button[2]")
        shortlist_btn.click()

        time.sleep(5)

class HandleShortlistCandidate:
    def perform_as(self, actor):
        wait = WebDriverWait(actor.driver, 20)
        
        # Esperar a que aparezca el formulario "Shortlist Candidate"
        form = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'oxd-form')]"))
        )
        
        # Hacer clic en el botón "Save" en el formulario "Shortlist Candidate"
        save_btn = form.find_element(By.XPATH, "//*[@type='submit']")
        save_btn.click()

        time.sleep(10)

class HandleScheduledStage:
    def perform_as(self, actor):
        wait = WebDriverWait(actor.driver, 20)
        
        # Esperar a que aparezca el formulario
        form = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'oxd-form')]"))
        )
        
        # Localizar el botón "Schedule" dentro del formulario
        schedule_btn = form.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div[1]/form/div[2]/div[2]/button[2]")
        schedule_btn.click()

        time.sleep(10)

class HandleInterviewPassed:
    def perform_as(self, actor):
        wait = WebDriverWait(actor.driver, 20)
        
        # Esperar a que aparezca el formulario
        form = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'oxd-form')]"))
        )
        
        # Localizar el botón "Interview" dentro del formulario
        interview_btn = form.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div[1]/form/div[2]/div[2]/button[2]")
        interview_btn.click()

        time.sleep(10)

class HandleOfferJob:
    def perform_as(self, actor):
        wait = WebDriverWait(actor.driver, 20)
        
        # Esperar a que aparezca el formulario
        form = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'oxd-form')]"))
        )
        
        # Localizar el botón "Offer Job" dentro del formulario
        offer_job_btn = form.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div[1]/form/div[2]/div[2]/button[2]")
        offer_job_btn.click()

        time.sleep(10)

class HandleHire:
    def perform_as(self, actor):
        wait = WebDriverWait(actor.driver, 20)
        
        # Esperar a que aparezca el formulario
        form = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'oxd-form')]"))
        )
        
        # Localizar el botón "Hire" dentro del formulario
        hire_btn = form.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div[1]/form/div[2]/div[2]/button[2]")
        hire_btn.click()

        time.sleep(10)
