#!/usr/bin/python3
'''Unittest for Console'''

from models import storage
from models.base_model import BaseModel
from unittest import TestCase
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO


class TestConsole(TestCase):
    '''Tests basic funtioning of the Console'''
    def setUp(self):
        self.con = HBNBCommand()


class test_create_user(TestCase):
    '''Test if create works for User and its attr'''
    def setUp(self):
        '''Setups up create user class tests'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User email="abc@gamil.com"\
                                 first_name="Betty"\
                                 last_name="Jane" password="xyz"')
            self.id = f.getvalue().strip()

    def test_user_attr(self):
        '''Test use attrs'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show User {self.id}')
            out = f.getvalue().strip()
            self.assertIn("'first_name': 'Betty'", out)
            self.assertIn("'last_name': 'Jane'", out)
            self.assertIn("'email': 'abc@gamil.com'", out)
            self.assertIn("'password': 'xyz'", out)


class test_create_place(TestCase):
    '''Tests create command for place model'''
    def setUp(self):
        '''Seup for place command'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place city_id="0001" user_id="0001"\
                                 name="My_little_house" number_rooms=4\
                                 number_bathrooms=2 max_guest=10\
                                 price_by_night=300 latitude=37.773972\
                                 longitude=-122.431297')
            self.id = f.getvalue().strip()

    def test_place_attr(self):
        '''Tests place attrs'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show Place {self.id}')
            out = f.getvalue().strip()
            self.assertIn("'number_bathrooms': '2'", out)
            self.assertIn("'longitude': '-122.431297'", out)
            self.assertIn("'city_id': '0001'", out)
            self.assertIn("'user_id': '0001'", out)
            self.assertIn("'latitude': '37.773972'", out)
            self.assertIn("'price_by_night': '300'", out)
            self.assertIn("'name': 'My little house'", out)
            self.assertIn("'max_guest': '10'", out)
            self.assertIn("'number_rooms': '4'", out)


class test_create_state(TestCase):
    '''Tests create command for state model'''
    def setUp(self):
        '''Seup for state command'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')
            self.id = f.getvalue().strip()

    def test_state_attr(self):
        '''Test state attrs'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show State {self.id}')
            out = f.getvalue().strip()
            self.assertIn("'name': 'California'", out)


class test_create_amenity(TestCase):
    '''Tests create command for state model'''
    def setUp(self):
        '''Seup for amenity command'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Amenity name="wifi"')
            self.id = f.getvalue().strip()

    def test_amenity_attr(self):
        '''test if attrs are correct'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show Amenity {self.id}')
            out = f.getvalue().strip()
            self.assertIn("'name': 'wifi'", out)


class test_create_review(TestCase):
    '''Tests create command for review model'''
    def setUp(self):
        '''Seup for create command'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Review place_id="002" user_id="002"\
                                 text="Good_place"')
            self.id = f.getvalue().strip()

    def test_review_attr(self):
        '''Test for appropriate place attr'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show Review {self.id}')
            out = f.getvalue().strip()
            self.assertIn("'place_id': '002'", out)
            self.assertIn("'user_id': '002'", out)
            self.assertIn("'text': 'Good place'", out)


class test_create_city(TestCase):
    '''Tests create command for city model'''
    def setUp(self):
        '''Seup for city command'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create City name="LA" state_id="009"')
            self.id = f.getvalue().strip()

    def test_city_attr(self):
        '''Test placee attrs'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show City {self.id}')
            out = f.getvalue().strip()
            self.assertIn("'name': 'LA'", out)
            self.assertIn("'state_id': '009'", out)
