import unittest
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    def test_new_instance_with_no_arguments(self):
        """Test creating a new instance of State with no arguments"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertIsNotNone(state.id)

    def test_new_instance_with_arguments(self):
        """Test creating a new instance of State with specific arguments"""
        data = {
            'id': 'some_id',
            'created_at': '2023-07-16T12:00:00.000000',
            'updated_at': '2023-07-16T13:00:00.000000',
            'name': 'Test State',
        }
        state = State(**data)
        self.assertIsInstance(state, State)
        self.assertEqual(state.id, 'some_id')
        self.assertEqual(str(state.created_at), '2023-07-16 12:00:00')
        self.assertEqual(str(state.updated_at), '2023-07-16 13:00:00')
        self.assertEqual(state.name, 'Test State')


if __name__ == '__main__':
    unittest.main()
