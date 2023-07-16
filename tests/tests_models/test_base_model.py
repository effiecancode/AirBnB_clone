#!/usr/bin/python3
import unittest
from datetime import datetime
from models import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_new_instance_with_no_arguments(self):
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertIsNotNone(model.id)

    def test_new_instance_with_arguments(self):
        data = {
            'id': 'some_id',
            'created_at': '2023-07-16T12:00:00.000000',
            'updated_at': '2023-07-16T13:00:00.000000',
            'name': 'Test Model',
            'value': 42
        }
        model = BaseModel(**data)
        self.assertIsInstance(model, BaseModel)
        self.assertEqual(model.id, 'some_id')
        self.assertEqual(str(model.created_at), '2023-07-16 12:00:00')
        self.assertEqual(str(model.updated_at), '2023-07-16 13:00:00')
        self.assertEqual(model.name, 'Test Model')
        self.assertEqual(model.value, 42)

    def test_new_instance_with_invalid_date_format(self):
        data = {
            'id': 'some_id',
            'created_at': '2023-07-16T12:00:00',
            'updated_at': '2023-07-16 13:00:00',
        }
        with self.assertRaises(ValueError):
            BaseModel(**data)

if __name__ == '__main__':
    unittest.main()