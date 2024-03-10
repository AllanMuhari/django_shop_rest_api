from contextlib import AbstractContextManager
from typing import Any
import unittest
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import  Location, Item
from .serializers import LocationSerializer, ItemSerializer
from django.urls import reverse


# Create your tests here.

class LocationTests(APITestCase):
    def test_create_location(self):
        """
        Ensure we can create a new location object.
        """
        url = reverse('location-list')
        data = {'name': 'Nairobi', 'address': '123 Main St'}
        response = self.client.post(url, data, format='json')
        location = Location.objects.get(pk=1)
        serializer = LocationSerializer(location)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serializer.data)

    def test_get_location(self):
        """
        Ensure we can get a location object.
        """
        location = Location.objects.create(name='Nairobi', address='123 Main St')
        url = reverse('location-detail', args=[location.id])
        response = self.client.get(url)
        serializer = LocationSerializer(location)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_location(self):
        """
        Ensure we can update a location object.
        """
        location = Location.objects.create(name='Nairobi', address='123 Main St')
        url = reverse('location-detail', args=[location.id])
        data = {'name': 'Uptown', 'address': '123 Main St'}
        response = self.client.put(url, data, format='json')
        location = Location.objects.get(pk=1)
        serializer = LocationSerializer(location)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_location(self):
        """
        Ensure we can delete a location object.
        """
        location = Location.objects.create(name='Nairobi', address='123 Main St')
        url = reverse('location-detail', args=[location.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # if __name__ == '__main__':
    #    unittest.main()