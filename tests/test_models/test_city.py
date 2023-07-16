import unittest
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    def test_new_instance_with_no_arguments(self):
        """Test creating a new instance of City with no arguments"""
        city = City()
        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertIsNotNone(city.id)

    def test_new_instance_with_arguments(self):
        """Test creating a new instance of City with specific arguments"""
        data = {
            'id': 'some_id',
            'created_at': '2023-07-16T12:00:00.000000',
            'updated_at': '2023-07-16T13:00:00.000000',
            'state_id': 'some_state_id',
            'name': 'Test City',
        }
        city = City(**data)
        self.assertIsInstance(city, City)
        self.assertEqual(city.id, 'some_id')
        self.assertEqual(str(city.created_at), '2023-07-16 12:00:00')
        self.assertEqual(str(city.updated_at), '2023-07-16 13:00:00')
        self.assertEqual(city.state_id, 'some_state_id')
        self.assertEqual(city.name, 'Test City')

    def test_new_instance_with_invalid_date_format(self):
        """Test creating a new instance of City with an invalid date format"""
        data = {
            'id': 'some_id',
            'created_at': '2023-07-16T12:00:00',
            'updated_at': '2023-07-16 13:00:00',
            'state_id': 'some_state_id',
            'name': 'Test City',
        }
        with self.assertRaises(ValueError):
            City(**data)


if __name__ == '__main__':
    unittest.main()
