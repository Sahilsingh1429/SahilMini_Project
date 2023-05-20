from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
    
    
    
class Product_Sub_Cat(models.Model):
    product_price = models.CharField(max_length=100)
    product_pic = models.FileField(upload_to='product_pic',default='happy.jpg')
    product_model = models.CharField(max_length=100)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product_price
    
    