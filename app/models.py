from django.db import models

class Profil(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=14) # +35569


    def __str__(self):
        return self.first_name + " " + self.last_name

class Product(models.Model):
    name_products = models.CharField(max_length=25)
    material = models.CharField(max_length=25)
    pay = models.FloatField(max_length=14)
    colour = models.CharField(max_length=25)
    photo = models.ImageField(null=True)

    def __str__(self):
        return self.name_products



# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
# python manage.py createsuperuser

