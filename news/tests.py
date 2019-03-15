from django.test import TestCase
from .models import Category,Location,Image

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Category(name = 'James')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Category))

    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)