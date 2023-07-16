import unittest
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    def test_new_instance_with_no_arguments(self):
        """Test creating a new instance of Review with no arguments"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)
        self.assertIsNotNone(review.id)

    def test_new_instance_with_arguments(self):
        """Test creating a new instance of Review with specific arguments"""
        data = {
            'id': 'some_id',
            'created_at': '2023-07-16T12:00:00.000000',
            'updated_at': '2023-07-16T13:00:00.000000',
            'place_id': 'some_place_id',
            'user_id': 'some_user_id',
            'text': 'Test review',
        }
        review = Review(**data)
        self.assertIsInstance(review, Review)
        self.assertEqual(review.id, 'some_id')
        self.assertEqual(str(review.created_at), '2023-07-16 12:00:00')
        self.assertEqual(str(review.updated_at), '2023-07-16 13:00:00')
        self.assertEqual(review.place_id, 'some_place_id')
        self.assertEqual(review.user_id, 'some_user_id')
        self.assertEqual(review.text, 'Test review')


if __name__ == '__main__':
    unittest.main()
