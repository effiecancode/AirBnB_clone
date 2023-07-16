#!/usr/bin/python3
"""Defines unittests for models/base_model.py file."""

import unittest
from models.base_model import BaseModel
from datetime import datetime, timedelta
import time
import sys

sys.path.append("/Users/mac/Alx/AirBnB_clone/tests/tests_models/test_base_model.py")
# module = __import__(BaseModel)

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


    def test_save_updates_updated_at(self):
        """Test if save function updates the updated_at attribute"""
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        updated_updated_at = self.base_model.updated_at

        self.assertNotEqual(initial_updated_at, updated_updated_at)
        self.assertTrue(updated_updated_at > initial_updated_at)

    def test_save_updates_created_at_on_new_instance(self):
        """Test if save function updates the created_at attribute on a new instance"""
        new_instance = BaseModel()
        self.assertIsInstance(new_instance.created_at, datetime)
        new_instance.save()

    def test_save_does_not_update_created_at_on_existing_instance(self):
        """Test if save function does not update the created_at attribute on an existing instance"""
        existing_instance = BaseModel()
        created_at_before_save = existing_instance.created_at
        existing_instance.save()
        created_at_after_save = existing_instance.created_at

        self.assertEqual(created_at_before_save, created_at_after_save)

    def test_save_updates_updated_at_on_existing_instance(self):
        """Test if save function updates the updated_at attribute on an existing instance"""
        existing_instance = BaseModel()
        existing_instance.save()  # Save the instance to set the initial updated_at value
        prev_updated_at = existing_instance.updated_at

        """Artificially set an older updated_at value to test the update"""
        existing_instance.updated_at = datetime.now() - timedelta(days=1)

        existing_instance.save()
        updated_at_after_save = existing_instance.updated_at

        self.assertNotEqual(prev_updated_at, updated_at_after_save)
        self.assertTrue(updated_at_after_save > prev_updated_at)

    def test_to_dict(self):
        data = {
            'id': '24',
            'created_at': '2023-07-16T12:00:00.000000',
            'updated_at': '2023-07-16T12:01:00.000000',
            'name': 'Effiecancode'
        }
        obj = BaseModel(**data)
        obj_dict = obj.to_dict()

        self.assertEqual(obj_dict['id'], '24')
        self.assertEqual(obj_dict['created_at'], '2023-07-16T12:00:00')
        self.assertEqual(obj_dict['updated_at'], '2023-07-16T12:01:00')
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['name'], 'Effiecancode')

    def test_to_dict_return_type(self):
        # Check if the return type is a dictionary
        result = self.base_model.to_dict()
        self.assertIsInstance(result, dict, "to_dict should return a dictionary")

    def test_to_dict_contains_all_attributes(self):
        # Check if all attributes are present in the dictionary
        result = self.base_model.to_dict()
        expected_attributes = ['id', 'created_at', 'updated_at', '__class__']
        for attribute in expected_attributes:
            self.assertIn(attribute, result, f"Attribute {attribute} should be present in the dictionary")

    def test_to_dict_datetime_format(self):
        # Check if 'created_at' and 'updated_at' are in the correct format
        result = self.base_model.to_dict()
        self.assertEqual(result['created_at'], self.base_model.created_at.isoformat(),
                         "The 'created_at' attribute should be in ISO format")
        self.assertEqual(result['updated_at'], self.base_model.updated_at.isoformat(),
                         "The 'updated_at' attribute should be in ISO format")

    def test_to_dict_class_name(self):
        # Check if the '__class__' attribute is correctly set to the class name
        result = self.base_model.to_dict()
        self.assertEqual(result['__class__'], 'BaseModel', "__class__ attribute should be set to 'BaseModel'")

    def test_to_dict_with_custom_attributes(self):
        # Check if custom attributes are correctly added to the dictionary
        self.base_model.custom_attribute = "custom_value"
        result = self.base_model.to_dict()
        self.assertEqual(result['custom_attribute'], "custom_value", "Custom attribute should be present in the dictionary")

    # def test_to_dict_with_updated_attribute(self):
    #     # Check if 'updated_at' attribute is updated when 'to_dict' is called
    #     old_updated_at = self.base_model.updated_at
    #     result = self.base_model.to_dict()
    #     new_updated_at = self.base_model.updated_at
    #     self.assertNotEqual(old_updated_at, new_updated_at,
    #                         "'updated_at' attribute should be updated when 'to_dict' is called")

if __name__ == '__main__':
    unittest.main()
