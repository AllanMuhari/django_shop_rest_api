from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Location, Item  
from .serializers import LocationSerializer, ItemSerializer
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class LocationTests(APITestCase):
    def test_create_location(self):
    #    Ensure we can create a new location object.
    
        url = reverse('location-list')
        data = {'name': 'Nairobi'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Location.objects.filter(name='Nairobi').exists())

    def test_get_location(self):
 
        # Ensure we can get a location object.
        
        location = Location.objects.create(name='Nairobi')
        url = reverse('location-detail', args=[location.pk])
        response = self.client.get(url)
        serializer = LocationSerializer(location)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_location(self):
          # Ensure we can get an update  object.
        location = Location.objects.create(name='Nairobi')
        url = reverse('location-detail', args=[location.pk])
        data = {'name': 'Uptown'}
        response = self.client.put(url, data, format='json')
        location.refresh_from_db()  # Refresh the instance to get updated values
        self.assertEqual(location.name, 'Uptown')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_location(self):
       # Ensure we can delete a location object.
        location = Location.objects.create(name='Nairobi')
        url = reverse('location-detail', args=[location.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Location.objects.filter(pk=location.pk).exists())

class LocationFormTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_access_create_location_form(self):
        # Navigate to the create location form page
        self.selenium.get(f'{self.live_server_url}/location/create/')  # Update URL as necessary
        # Check if the form is present
        form_present = self.selenium.find_elements(By.ID, "location-form")  # Assume the form has this ID
        self.assertTrue(len(form_present) > 0)

    def test_submit_create_location_form(self):
        # Navigate to the create location form page
        self.selenium.get(f'{self.live_server_url}/location/create/')  # Update URL as necessary
        # Assume form fields have names 'name' and 'address', adjust if different
        self.selenium.find_element(By.NAME, 'name').send_keys('Test Location')
        # Submit the form
        self.selenium.find_element(By.CSS_SELECTOR, 'form input[type="submit"]').click()
        # Verify redirection or form submission result, e.g., by checking a success message
        # This part depends on your application's response to form submission