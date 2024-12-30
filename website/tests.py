from django.test import TestCase
from .models import Record

class RecordModelTestCase(TestCase):
    def setUp(self):
        # Set up some test data for the model
        self.record_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone': '123-456-7890',
            'address': '123 Main St',
            'city': 'Example City',
            'state': 'Example State',
            'zipcode': '12345',
        }
        self.record = Record.objects.create(**self.record_data)

    def test_record_str_method(self):
        # Test the __str__ method of the Record model
        expected_str = f"{self.record_data['first_name']} {self.record_data['last_name']}"
        self.assertEqual(str(self.record), expected_str)

    def test_record_attributes(self):
        # Test each attribute of the Record model
        self.assertEqual(self.record.first_name, self.record_data['first_name'])
        self.assertEqual(self.record.last_name, self.record_data['last_name'])
        self.assertEqual(self.record.email, self.record_data['email'])
        self.assertEqual(self.record.phone, self.record_data['phone'])
        self.assertEqual(self.record.address, self.record_data['address'])
        self.assertEqual(self.record.city, self.record_data['city'])
        self.assertEqual(self.record.state, self.record_data['state'])
        self.assertEqual(self.record.zipcode, self.record_data['zipcode'])

    def test_record_created_at(self):
        # Test the created_at attribute (auto_now_add=True)
        # created_at should not be provided by the user but should be auto-set
        self.assertIsNotNone(self.record.created_at)

    # Add more test cases if needed
