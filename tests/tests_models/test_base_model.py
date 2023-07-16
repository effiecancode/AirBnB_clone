#!/usr/bin/python3
"""Defines unittests for models/base_model.py file."""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import time
import sys

sys.path.append("/Users/mac/Alx/AirBnB_clone/tests/tests_models/test_base_model.py")
# module = __import__(BaseModel)

class TestBaseModel(unittest.TestCase):

    def test_init_with_kwargs(self):
        data = {
            'id': '123',
            'created_at': '2023-07-16T12:00:00.000000',
            'updated_at': '2023-07-16T12:01:00.000000',
            'name': 'test object'
        }
        obj = BaseModel(**data)

        self.assertEqual(obj.id, '123')
        self.assertEqual(obj.created_at, datetime(2023, 7, 16, 12, 0))
        self.assertEqual(obj.updated_at, datetime(2023, 7, 16, 12, 1))
        self.assertEqual(obj.name, 'test object')

    def test_init_without_kwargs(self):
        obj = BaseModel()

        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_save(self):
        obj = BaseModel()
        prev_updated_at = obj.updated_at
        obj.save()

        self.assertNotEqual(prev_updated_at, obj.updated_at)

    def test_to_dict(self):
        data = {
            'id': '123',
            'created_at': '2023-07-16T12:00:00.000000',
            'updated_at': '2023-07-16T12:01:00.000000',
            'name': 'test object'
        }
        obj = BaseModel(**data)
        obj_dict = obj.to_dict()

        self.assertEqual(obj_dict['id'], '123')
        self.assertEqual(obj_dict['created_at'], '2023-07-16T12:00:00')
        self.assertEqual(obj_dict['updated_at'], '2023-07-16T12:01:00')
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['name'], 'test object')

if __name__ == '__main__':
    unittest.main()
