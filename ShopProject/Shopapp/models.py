from django.db import models

# Create your models here.
class Eshop(models.Model):
    shop_id = models.IntegerField(primary_key=True)
    shop_name = models.CharField(max_length=100)
    shop_address = models.CharField(max_length=100)
    phone_number = models.BigIntegerField()
    email = models.EmailField()
    prodcut_name = models.CharField(max_length=100)
    product_category = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to = 'ProductPhotos/')
    product_price = models.FloatField()

    def __str__(self):
        return str(self.shop_id)
