from unittest import TestCase
from main import folder_create

class TestYaDisk(TestCase):

    def test_ya_disk_folder(self):
        result = folder_create('test_folder')
        self.assertIn(result, (201, 409))
