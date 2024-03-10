from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Location, Item  
from .serializers import LocationSerializer, ItemSerializer

class LocationTests(APITestCase):
    def test_create_location(self):
        """
        Ensure we can create a new location object.
        """
        url = reverse('location-list')
        data = {'name': 'Nairobi'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Location.objects.filter(name='Nairobi').exists())

    def test_get_location(self):
        """
        Ensure we can get a location object.
        """
        location = Location.objects.create(name='Nairobi')
        url = reverse('location-detail', args=[location.pk])
        response = self.client.get(url)
        serializer = LocationSerializer(location)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_location(self):
        """
        Ensure we can update a location object.
        """
        location = Location.objects.create(name='Nairobi')
        url = reverse('location-detail', args=[location.pk])
        data = {'name': 'Uptown'}
        response = self.client.put(url, data, format='json')
        location.refresh_from_db()  # Refresh the instance to get updated values
        self.assertEqual(location.name, 'Uptown')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_location(self):
        """
        Ensure we can delete a location object.
        """
        location = Location.objects.create(name='Nairobi')
        url = reverse('location-detail', args=[location.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Location.objects.filter(pk=location.pk).exists())
