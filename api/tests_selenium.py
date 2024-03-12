from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminInterfaceTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = webdriver.ChromeOptions()
        cls.selenium = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_add_and_delete_location(self):
     
        self.selenium.get(f'{self.live_server_url}/admin/login/')
        
        # Log in
        username_input = self.selenium.find_element(By.NAME, 'username')
        password_input = self.selenium.find_element(By.NAME, 'password')
        submit_button = self.selenium.find_element(By.XPATH, '//input[@type="submit"]')

        username_input.send_keys('allan')
        password_input.send_keys('1111')

        submit_button.click()

        
       
        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Log out'))
        )
        
        self.selenium.get('http://127.0.0.1:8000/admin/api/location/')
        
        
        add_button = WebDriverWait(self.selenium, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.add-link-specific'))
        )
        add_button.click()
        
    


    
