from django.db import models

# Create your models here.
class Restaurant(models.Model):
    Restaurant_name = models.CharField(max_length=30)
    Restaurant_city= models.CharField(max_length=30)
    Restaurant_description=models.CharField(max_length=1000)
    Restaurant_contact_no= models.IntegerField(max_length=10)
    image = models.ImageField(default= 'abc.jpg',upload_to = 'Images')
    
    class Meta:
        db_table = "Restaurant"
       
class menucategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "menucategory"

    def __str__(self):
        return self.name 
 
class menuitem(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=500)
    cat_fk = models.ForeignKey(menucategory, on_delete=models.CASCADE)
    image = models.ImageField(default= 'abc.jpg',upload_to = 'Images')

    class Meta:
        db_table = "menuitem"

    def __str__(self):
        return self.name
    
class Accounts(models.Model):
    cardno = models.CharField(max_length=4)
    cvv = models.CharField(max_length=4)
    expiry = models.CharField(max_length=10)
    balance = models.FloatField(default=20000)

    class Meta:
        db_table = "Accounts"