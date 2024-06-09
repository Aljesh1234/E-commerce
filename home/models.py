from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=300,unique=True)
    logo = models.CharField(max_length=300)
    slug = models.CharField(max_length=300,unique=True)
    def __str__(self):
        return self.name



class Slider(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    url = models.URLField(max_length=500,blank=True)
    rank = models.IntegerField()
    def __str__(self):
        return self.name

class ADD(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    rank = models.IntegerField()
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    rank = models.IntegerField()
    slug = models.CharField(max_length=300,unique=True)
    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    comment = models.TextField()
    post = models.CharField(max_length=300)
    stars = models.IntegerField()
    def __str__(self):
        return self.name

class StieInfo(models.Model):
    address = models.TextField()
    email = models.EmailField(max_length=500)
    phone = models.CharField(max_length=300)
    Twitter = models.URLField(max_length=500,blank=True)
    facebook = models.URLField(max_length=500,blank=True)
    Instagram = models.URLField(max_length=500,blank=True)
    youtube = models.URLField(max_length=500,blank=True)
    linkedin = models.URLField(max_length=500,blank=True)
    def __str__(self):
        return self.name

STOCK = (('In Stock','In Stock'),('Out of Stock','Out of Stock'))
LABELS = (('default','default'),('hot','hot'),('new','new'),('sale','sale'))
class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    discounted_price = models.IntegerField()
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    specification = models.TextField(blank=True)
    slug = models.TextField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    stock = models.CharField(max_length=100,choices=STOCK)
    labels = models.CharField(max_length=100, choices=LABELS)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id', "name", 'price','category')

class ProductReviews(models.Model):
    username = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    date = models.DateField(auto_now=True)
    star = models.IntegerField()
    review = models.TextField()
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='media',null=True)
    def __str__(self):
        return self.username





class Cart(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    quantity = models.IntegerField()
    total = models.IntegerField()
    slug = models.SlugField(max_length=500)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    checkout = models.BooleanField(default=False)
    def __str__(self):
        return self.name