from django.test import TestCase
from .models import Category,Photo
# Create your tests here.

class CategoryTest(TestCase):
    def setUp(self):
        self.category = Category(name='food')
        self.category.save_category()
        
        
    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        cat = Category.objects.all()
        self.assertTrue(len(cat) > 0)