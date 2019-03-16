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
        self.james.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

        
class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new location and saving it
        self.james= Location(name = 'James')
        self.james.save_location()

        # Creating a new category and saving it
        self.new_category = Category(name = 'testing')
        self.new_category.save()

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()
    
    def test_get_news_today(self):
        news_of_days = Image.news_of_days()
        self.assertTrue(len(news_of_days)>0)

    

   
   