import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test base model class"""
    def test_new_instance_with_no_arguments(self):
        """Test creating a new instance of BaseModel with no arguments"""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertIsNotNone(model.id)

    def test_new_instance_with_arguments(self):
        """Test creating a new instance of BaseModel with specific arguments"""
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
        """Test creating a new instance of BaseModel
        with an invalid date format"""
        data = {
            'id': 'some_id',
            'created_at': '2023-07-16T12:00:00',
            'updated_at': '2023-07-16 13:00:00',
        }
        with self.assertRaises(ValueError):
            BaseModel(**data)

    def test_save_updates_updated_at(self):
        """Test that calling save() method updates
        the updated_at attribute"""
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)

    def test_to_dict_returns_correct_dict(self):
        """Test that the to_dict() method returns the
        expected dictionary representation"""
        md = BaseModel()
        model_dict = md.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], md.id)
        self.assertEqual(model_dict['created_at'], md.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], md.updated_at.isoformat())

    def test_str_representation(self):
        """Test that the __str__() method returns the
        expected string representation"""
        model = BaseModel()
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_str)


if __name__ == '__main__':
    unittest.main()
