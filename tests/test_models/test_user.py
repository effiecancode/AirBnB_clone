import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    def test_new_instance_with_no_arguments(self):
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)
        self.assertIsNotNone(user.id)

    def test_new_instance_with_arguments(self):
        data = {
            'id': 'some_id',
            'created_at': '2023-07-16T12:00:00.000000',
            'updated_at': '2023-07-16T13:00:00.000000',
            'email': 'test@example.com',
            'password': 'test_password',
            'first_name': 'John',
            'last_name': 'Doe',
        }
        user = User(**data)
        self.assertIsInstance(user, User)
        self.assertEqual(user.id, 'some_id')
        self.assertEqual(str(user.created_at), '2023-07-16 12:00:00')
        self.assertEqual(str(user.updated_at), '2023-07-16 13:00:00')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.password, 'test_password')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')


if __name__ == '__main__':
    unittest.main()
