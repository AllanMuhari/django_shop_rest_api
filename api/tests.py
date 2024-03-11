from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  

class AdminInterfaceTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login_and_list_locations_in_admin(self):
        # Navigate to the Django admin login page
        self.selenium.get(f'{self.live_server_url}/admin/')

        # Find the login form inputs and submit button
        username_input = self.selenium.find_element(By.NAME, 'username')
        password_input = self.selenium.find_element(By.NAME, 'password')
        submit_button = self.selenium.find_element(By.XPATH, '//input[@type="submit"]')

        # Fill out the form with your superuser's credentials
        username_input.send_keys('allan')
        password_input.send_keys('1111')

        # Submit the form to log in
        submit_button.click()

        # Navigate to the Locations model in the admin.
        self.selenium.get(f'{self.live_server_url}/admin/api/location')

        # Use WebDriverWait to wait for the change list element to become visible
        WebDriverWait(self.selenium, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'change-list'))
        )

        # Now that we've waited for it to be visible, find the element
        change_list = self.selenium.find_element(By.CLASS_NAME, 'change-list')
        self.assertTrue(change_list.is_displayed())

