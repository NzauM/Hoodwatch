from django.test import TestCase
from .models import Posts,Profile,Business,Neighborhood
from django.contrib.auth.models import User
import unittest

# Create your tests here.
class Neighborhoodtestcase(TestCase):
    '''
    Class to test all neighbourhood model methods
    '''
    def setUp(Self):
        '''
        Function to create new instance of a neighbourhood class
        '''
        self.hood=Neighborhood(hoodname='Karen',hoodlocation='Nairobi',pic='pic.jpg',description='cool hood',police_count=2,police_info='info@gmail',
        occupant=2,health=1,health_info='health@hdj.com')
        Self.hood.save()

    def test_instance(self):
        '''
        Test neighbourhood class instantiation
        '''
        self.assertTrue(isinstance(self.hood,Neighborhood))

    def tearDown(self):
        '''
        Function to delete every test instance after it runs
        '''
        Neighborhood.objects.all().delete()

    def create_hood_test(self):
        '''
        Tests that a new hood is saved 
        '''
        self.hood.create_hood()
        hoodlist = Neighborhood.objects.all()
        self.assertTrue(len(hoodlist)==1)

    def delete_hood_test(self):
        '''
        Tests that a Neighborhood instance can be deleted
        '''
        self.hood.save()
        self.hood.delete()
        hoodlist = Neighborhood.objects.all()
        self.assertEqual(len(hoodlist,0))

    

