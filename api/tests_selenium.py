from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LocationAdminTest(StaticLiveServerTestCase):
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
        self.selenium.get(f'{self.live_server_url}/admin/api/location/')


        self.selenium.find_element(By.CSS_SELECTOR, 'a.addlink').click()
        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.NAME, 'name'))
        )
        
        self.selenium.find_element(By.NAME, 'name').send_keys('New Location')
    
        self.selenium.find_element(By.NAME, '_save').click()

    
