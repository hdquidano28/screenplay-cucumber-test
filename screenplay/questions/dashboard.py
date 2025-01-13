from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardIsVisible:
    def answer_as(self, actor):
        try:
            wait = WebDriverWait(actor.driver, 10)
            dashboard = wait.until(
                EC.presence_of_element_located((By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']"))
            )
            return dashboard.is_displayed()
        except:
            return False