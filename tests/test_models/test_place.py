import unittest
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_new_instance_with_no_arguments(self):
        """Test creating a new instance of Place with no arguments"""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertTrue(hasattr(place, 'id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)
        self.assertIsNotNone(place.id)

    def test_new_instance_with_arguments(self):
        """Test creating a new instance of Place with specific arguments"""
        data = {
            'id': 'some_id',
            'created_at': '2023-07-16T12:00:00.000000',
            'updated_at': '2023-07-16T13:00:00.000000',
            'city_id': 'some_city_id',
            'user_id': 'some_user_id',
            'name': 'Test Place',
            'description': 'Some description',
            'number_rooms': 2,
            'number_bathrooms': 2,
            'max_guest': 4,
            'price_by_night': 100,
            'latitude': 37.7749,
            'longitude': -122.4194,
            'amenity_ids': ['amenity_1', 'amenity_2']
        }
        place = Place(**data)
        self.assertIsInstance(place, Place)
        self.assertEqual(place.id, 'some_id')
        self.assertEqual(str(place.created_at), '2023-07-16 12:00:00')
        self.assertEqual(str(place.updated_at), '2023-07-16 13:00:00')
        self.assertEqual(place.city_id, 'some_city_id')
        self.assertEqual(place.user_id, 'some_user_id')
        self.assertEqual(place.name, 'Test Place')
        self.assertEqual(place.description, 'Some description')
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertAlmostEqual(place.latitude, 37.7749)
        self.assertAlmostEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ['amenity_1', 'amenity_2'])


if __name__ == '__main__':
    unittest.main()
