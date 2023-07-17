import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_new_instance_with_no_arguments(self):
        """Test creating a new instance of Amenity with no arguments """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertIsNotNone(amenity.id)

    def test_new_instance_with_arguments(self):
        """Test creating a new instance of Amenity with specific arguments"""
        data = {
            'id': 'some_id',
            'created_at': '2023-07-16T12:00:00.000000',
            'updated_at': '2023-07-16T13:00:00.000000',
            'name': 'Test Amenity',
        }
        amenity = Amenity(**data)
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.id, 'some_id')
        self.assertEqual(str(amenity.created_at), '2023-07-16 12:00:00')
        self.assertEqual(str(amenity.updated_at), '2023-07-16 13:00:00')
        self.assertEqual(amenity.name, 'Test Amenity')

    def test_new_instance_with_invalid_date_format(self):
        """Test creating a new instance of Amenity with
        an invalid date format"""
        data = {
            'id': 'some_id',
            'created_at': '2023-07-16T12:00:00',
            'updated_at': '2023-07-16 13:00:00',
            'name': 'Test Amenity',
        }
        with self.assertRaises(ValueError):
            Amenity(**data)


if __name__ == '__main__':
    unittest.main()
