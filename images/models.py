from django.db import models


class Location(models.Model):
    location_name = models.CharField(max_length=45)

    def __str__(self):
        return self.location_name

    def save_location(self):
        return self.save()


class Category(models.Model):
    category_name = models.CharField(max_length=16)

    def __str__(self):
        return self.category_name

    def save_category(self):
        return self.save()


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    Name = models.CharField(max_length=20)
    Description = models.CharField(max_length=45)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.Name

    def save_image(self):
        return self.save()

    class Meta:
        ordering = ['image']

    @classmethod
    def search_by_title(cls, search_term):
        images = cls.objects.filter(Name__icontains=search_term)
        return images
