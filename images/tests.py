from django.test import TestCase
from .models import Image, Location, Category
# Create your tests here.


class ImageTestClass(TestCase):
    def setUp(self):
        self.category = Category(category_name="Potraits")
        self.location = Location(location_name="Roof-top")
        self.new_image = Image(image='images/Screenshot_2019-05-10-12-08-06-04.png',
                               Name='NINDO', Description='Love prolly', location_id=1, category_id=1)

    def test_instance(self):
        self.location.save()
        self.category.save()
        self.new_image.save()
        self.assertTrue(isinstance(self.new_image, Image))


class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(location_name="Roof-top")

    def test_instance(self):
        self.location.save()
        self.assertTrue(isinstance(self.location, Location))


class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(category_name="Potraits")

    def test_instance(self):
        self.category.save()
        self.assertTrue(isinstance(self.category, Category))

    def test_save(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)
