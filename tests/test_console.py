#! /usr/bin/python3
"""tests for console"""
import unittest
from unittest.mock import patch
import io
from console import HBNBCommand


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
        inst_id = 'instance_id'
        inst_repr = 'Instance Representation'
        my_var = 'models.storage.all'
        with patch(my_var, return_value={f'BaseModel.{inst_id}': inst_repr}), \
             patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.console.do_show('BaseModel {}'.format(inst_id))
            output = fake_stdout.getvalue().strip()
            self.assertEqual(output, inst_repr)

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


if __name__ == '__main__':
    unittest.main()
