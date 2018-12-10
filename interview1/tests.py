from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Location
from decimal import *
import psycopg2

class APIInterview12Tests(APITestCase):

    def setUp(self) :
        self.location1 = Location.objects.create(pincode='IN/201001',address='Shastri nagar',city='Ghaziabad',lat=28.6733,lng=77.4731)
        self.location2 = Location.objects.create(pincode='IN/201005',address='Raj nagar',city='Ghaziabad',lat=28.6821,lng=77.4444)
        self.location3 = Location.objects.create(pincode='IN/201002',address='Kavi nagar',city='Ghaziabad',lat=28.6636,lng=77.4519)
        self.location4 = Location.objects.create(pincode='IN/201012',address='Vasundhara',city='Ghaziabad',lat=28.6636,lng=77.3698)
        self.location5 = Location.objects.create(pincode='IN/201014',address='Indirapuram',city='Ghaziabad',lat=28.6415,lng=77.3714)

    def test_interview1a(self):
        url = reverse('postloc')
        data = {'pincode': 'IN/201008','address':'Sanjay nagar','city':'Ghaziabad','lat':'21.6733','lng':'71.4731'}
        response = self.client.post(url, data)
        self.assertEqual(Location.objects.count(), 6)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_interview1b(self):
        url = reverse('postloc')
        data = {'pincode': 'IN/201001','address':'Shastri nagar','city':'Ghaziabad','lat':'28.6733','lng':'77.4731'}
        response = self.client.post(url, data)
        self.assertEqual(Location.objects.count(), 5)

    def test_interview1c(self):
        url = reverse('postloc')
        data = {'pincode': 'IN/201001','address':'Hera nagar','city':'Ghaziabad','lat':'20.6733','lng':'70.4731'}
        response = self.client.post(url, data)
        self.assertEqual(Location.objects.count(), 5)

    def test_interview1d(self):
        url = reverse('postloc')
        data = {'pincode': 'IN/201009','address':'Subh nagar','city':'Ghaziabad','lat':'28.68','lng':'77.48'}
        response = self.client.post(url, data)
        self.assertEqual(Location.objects.count(), 5)

    def test_interview2a(self):
        url = reverse('getself')
        data = {'lat': '28.6733','lng':'77.4731','radius':'5'}
        response = self.client.post(url, data)
        self.assertEqual(response.data,{'data':[('IN/201001','Shastri nagar','Ghaziabad'),('IN/201005','Raj nagar','Ghaziabad'),('IN/201002','Kavi nagar','Ghaziabad')]})

    def test_interview2b(self):
        url = reverse('getself')
        data = {'lat': '28.6733','lng':'77.4731','radius':'20'}
        response = self.client.post(url, data)
        self.assertEqual(response.data,{'data':[('IN/201001','Shastri nagar','Ghaziabad'),('IN/201005','Raj nagar','Ghaziabad'),('IN/201002','Kavi nagar','Ghaziabad'),('IN/201012','Vasundhara','Ghaziabad'),('IN/201014','Indirapuram','Ghaziabad')]})

    # def test_interview2(self):
    #     conn = psycopg2.connect(database='apitest',user='postgres',password='Prerna2110',host='localhost')
    #     url = reverse('getpos')
    #     data = {'lat': '23.5500','lng':'74.8667','radius':'5'}
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.data,{'data':[("IN/854330","Kasba","Bihar"),("IN/854333","Madanpur Purnia","Bihar"),("IN/854335","Narpalganj","Bihar"),("IN/854336","Nawabganj","Bihar"),("IN/854339","Balua Bazar","Bihar")]})
    #     conn.close()

    def tearDown(self) :
        Location.objects.all().delete()
