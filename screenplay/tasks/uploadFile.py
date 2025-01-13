from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import pyautogui
from pathlib import Path

class UploadFile:
    def __init__(self, file_name):
        self.file_name = file_name
        
    def _validate_pdf(self, file_path):
        """Validate if the file is a PDF and exists"""
        if not file_path.exists():
            raise FileNotFoundError(f"PDF file not found: {file_path}")
        if not file_path.suffix.lower() == '.pdf':
            raise ValueError(f"File must be a PDF: {file_path}")
            
    def perform_as(self, actor):
        wait = WebDriverWait(actor.driver, 10)
        
        # Use the specific file path
        file_path = Path('file/resume.pdf')
        file_path = file_path.absolute()
        self._validate_pdf(file_path)
        
        try:
            # Wait for and click the upload button
            upload_div = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "oxd-file-div"))
            )
            browse_button = upload_div.find_element(By.CLASS_NAME, "oxd-file-button")
            browse_button.click()
            
            # Small delay for file dialog
            time.sleep(2)
            
            # Handle file dialog with specific file path
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')
            pyautogui.write(str(file_path))
            time.sleep(2)
            pyautogui.press('enter')
            
            # Verify upload success
            wait.until(
                lambda driver: "No file selected" not in 
                driver.find_element(By.CLASS_NAME, "oxd-file-input-div").text
            )
            
            print(f"✓ PDF uploaded successfully: TEXT.txt")
            
        except Exception as e:
            print(f"❌ Error uploading PDF: {str(e)}")
            raise