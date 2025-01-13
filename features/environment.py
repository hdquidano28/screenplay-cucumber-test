from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
import pyautogui
from pathlib import Path

def before_all(context):
    # Configure PyAutoGUI settings
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 1
    
    # Setup Firefox driver
    service = Service(EdgeChromiumDriverManager().install())

    # Inicializar el navegador Edge
    context.driver = webdriver.Edge(service=service)

    # Maximizar la ventana del navegador
    context.driver.maximize_window()
    
    # Ensure file directory exists
    Path('file').mkdir(exist_ok=True)

def after_all(context):
    context.driver.quit()