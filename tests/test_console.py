#! /usr/bin/python3
"""tests for console"""
import unittest
from unittest.mock import patch
import io
import sys
import ast
from console import HBNBCommand


sys.path.append("/home/njuguna/Desktop/alx/SE foundations/AirBnB_clone/")


class TestHBNBCommand(unittest.TestCase):
    """Test cases for HBNBCommand"""

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    def test_quit(self):
        """Test quit command"""
        with self.assertRaises(SystemExit):
            self.console.do_quit('')

    def test_EOF(self):
        """Test EOF command"""
        with self.assertRaises(SystemExit):
            self.console.do_EOF('')

    def test_emptyline(self):
        """Test emptyline method"""
        self.assertEqual(self.console.lastcmd, '')

    def test_create_missing_class_name(self):
        """Test create command with missing class name"""
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_create('')
            output = fake_stdout.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_create_invalid_class_name(self):
        """Test create command with invalid class name"""
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_create('InvalidClass')
            output = fake_stdout.getvalue().strip()
            self.assertEqual(output, '** class doesn\'t exist **')

    def test_create_valid_class_name(self):
        """Test create command with valid class name"""
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_create('BaseModel')
            output = fake_stdout.getvalue().strip()
            self.assertRegex(output, r'^[0-9a-f-]{36}$')

    def test_show_missing_class_name(self):
        """Test show command with missing class name"""
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_show('')
            output = fake_stdout.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_show_invalid_class_name(self):
        """Test show command with invalid class name"""
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_show('InvalidClass')
            output = fake_stdout.getvalue().strip()
            self.assertEqual(output, '** class doesn\'t exist **')

    def test_show_missing_instance_id(self):
        """Test show command with missing instance ID"""
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_show('BaseModel')
            output = fake_stdout.getvalue().strip()
            self.assertEqual(output, '** instance id missing **')

    def test_show_no_instance_found(self):
        """Test show command with no instance found"""
        with patch('models.storage.all', return_value={}), \
             patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_show('BaseModel instance_id')
            output = fake_stdout.getvalue().strip()
            self.assertEqual(output, '** no instance found **')

    def test_show_valid(self):
        """Test show command with valid class name and instance ID"""
        instance_id = 'instance_id'
        instance_repr = 'Instance Representation'
        return_value = {'BaseModel.{}'.format(instance_id): instance_repr}
        with patch('models.storage.all', return_value), \
             patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_show('BaseModel {}'.format(instance_id))
            output = fake_stdout.getvalue().strip()
            self.assertEqual(output, instance_repr)

    def test_destroy_missing_class_name(self):
        """Test destroy command with missing class name"""
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_destroy('')
            output = fake_stdout.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_destroy_invalid_class_name(self):
        """Test destroy command with invalid class name"""
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_destroy('InvalidClass')
            output = fake_stdout.getvalue().strip()
            self.assertEqual(output, '** class doesn\'t exist **')

    def test_destroy_missing_instance_id(self):
        """Test destroy command with missing instance ID"""
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_destroy('BaseModel')
            output = fake_stdout.getvalue().strip()
            self.assertEqual(output, '** instance id missing **')

    def test_destroy_no_instance_found(self):
        """Test destroy command with no instance found"""
        with patch('models.storage.all', return_value={}), \
             patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_destroy('BaseModel instance_id')
            output = fake_stdout.getvalue().strip()
            self.assertEqual(output, '** no instance found **')

    def test_destroy_valid(self):
        """Test destroy command with valid class name and instance ID"""
        instance_id = 'instance_id'
        instance_key = 'BaseModel.{}'.format(instance_id)
        my_var = 'models.storage.all'
        with patch(my_var, return_value={instance_key: 'Instance'}), \
             patch('models.storage.save'), \
             patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_destroy('BaseModel {}'.format(instance_id))
            output = fake_stdout.getvalue().strip()
            self.assertEqual(output, '')

    def test_all_invalid_class_name(self):
        """Test all command with invalid class name"""
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_all('InvalidClass')
            output = fake_stdout.getvalue().strip()
            self.assertEqual(output, '** class doesn\'t exist **')

    def test_all_valid(self):
        """Test all command with valid class name"""
        instance1 = 'Instance1'
        instance2 = 'Instance2'
        with patch('models.storage.all', return_value={
                'BaseModel.1': instance1,
                'BaseModel.2': instance2
        }), patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_all('BaseModel')
            output = fake_stdout.getvalue().strip()
            self.assertRegex(output, r'^\[.*\]$')
            instances = ast.literal_eval(output)
            self.assertIn(instance1, instances)
            self.assertIn(instance2, instances)

    def test_update_missing_class_name(self):
        """Test update command with missing class name"""
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_update('')
            output = fake_stdout.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_update_invalid_class_name(self):
        """Test update command with invalid class name"""
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_update('InvalidClass')
            output = fake_stdout.getvalue().strip()
            self.assertEqual(output, '** class doesn\'t exist **')

    def test_update_missing_instance_id(self):
        """Test update command with missing instance ID"""
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_update('BaseModel')
            output = fake_stdout.getvalue().strip()
            self.assertEqual(output, '** instance id missing **')

    def test_update_missing_attribute_dict(self):
        """Test update command with missing attribute dictionary"""
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_update('BaseModel instance_id')
            output = fake_stdout.getvalue().strip()
            self.assertEqual(output, '** attribute dictionary missing **')

    def test_update_invalid_attribute_dict(self):
        """Test update command with invalid attribute dictionary"""
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_update('BaseModel instance_id InvalidDictionary')
            output = fake_stdout.getvalue().strip()
            self.assertEqual(output, '** invalid attribute dictionary **')

    def test_update_valid(self):
        """Test update command with valid class, ID, and dictionary"""
        instance_id = 'instance_id'
        instance_key = 'BaseModel.{}'.format(instance_id)
        attribute_dict = {'first_name': 'John', 'age': 89}
        my_dict = 'models.storage.all'
        with patch(my_dict, return_value={instance_key: 'Instance'}), \
             patch('models.storage.save'), \
             patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_update(f'BaseModel {instance_id} {attribute_dict}')
            output = fake_stdout.getvalue().strip()
            self.assertEqual(output, '')
            new_var = self.console.all()[instance_key]
            self.assertEqual(new_var.first_name, 'John')
            self.assertEqual(new_var.age, 89)

    def test_count_missing_class_name(self):
        """Test count command with missing class name"""
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_count('')
            output = fake_stdout.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_count_invalid_class_name(self):
        """Test count command with invalid class name"""
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_count('InvalidClass')
            output = fake_stdout.getvalue().strip()
            self.assertEqual(output, '** class doesn\'t exist **')

    def test_count_valid(self):
        """Test count command with valid class name"""
        instance1 = 'Instance1'
        instance2 = 'Instance2'
        with patch('models.storage.all', return_value={
                'BaseModel.1': instance1,
                'BaseModel.2': instance2
        }), patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_count('BaseModel')
            output = fake_stdout.getvalue().strip()
            self.assertEqual(output, '2')


if __name__ == '__main__':
    unittest.main()
