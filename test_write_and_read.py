import unittest
import os
from file_write_read import write_to_file, read_from_file

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        self.file_name = 'test_file.json'
        self.test_data = {
            "pk": 4,
            "title": "Test Title",
            "author": "Test Author",
            "published_date": "2024-06-23",
            "publisher": 6,
            "price": 9.99,
            "discounted_price": 3.56,
            "is_bestseller": True,
            "is_banned": False,
            "genres": [1]
        }

    def tearDown(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

    def test_write_and_read_file(self):
        write_to_file(self.file_name, self.test_data)
        read_data = read_from_file(self.file_name)
        self.assertEqual(read_data['pk'], 4)
        self.assertEqual(read_data['title'], "Test Title")
        self.assertEqual(read_data['author'], "Test Author")
        self.assertEqual(read_data['published_date'], "2024-06-23")
        self.assertEqual(read_data['publisher'], 6)
        self.assertEqual(read_data['price'], 9.99)
        self.assertEqual(read_data['discounted_price'], 3.56)
        self.assertEqual(read_data['is_bestseller'], True)
        self.assertEqual(read_data['is_banned'], False)
        self.assertEqual(read_data['genres'], [1])

    def test_write_and_read_empty_file(self):
        empty_data = {}
        write_to_file(self.file_name, empty_data)
        read_data = read_from_file(self.file_name)
        self.assertEqual(read_data, {})

    def test_read_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file('nonexistent_file.json')

    def test_write_bad_data_into_file(self):
        bad_data = { "set_data": {1, 2, 3} }
        with self.assertRaises(TypeError):
            write_to_file(self.file_name, bad_data)

if __name__ == '__main__':
    unittest.main()