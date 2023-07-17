import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        """Clean up the test environment"""
        self.storage._FileStorage__objects = {}
        self.storage.save()


    def test_all(self):
        """Test the all method"""
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """Test the new method"""
        model = BaseModel()
        self.storage.new(model)
        self.assertIn(f"BaseModel.{model.id}", self.storage.all())

    def test_save_reload(self):
        """Test the save and reload methods"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()

        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()
        self.assertIn(f"BaseModel.{model.id}", new_storage.all())

    def test_save_reload_multiple_objects(self):
        """Test the save and reload methods with multiple objects"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.storage.new(model1)
        self.storage.new(model2)
        self.storage.save()

        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()
        self.assertIn(f"BaseModel.{model1.id}", new_storage.all())
        self.assertIn(f"BaseModel.{model2.id}", new_storage.all())


if __name__ == '__main__':
    unittest.main()
