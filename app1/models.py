from django.db import models

# Create your models here.
from django.db import models 
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    profile_id=models.OneToOneField(User,on_delete=models.CASCADE)
    Nnikename=models.CharField(max_length=32)
    Adhaar_card_No = models.IntegerField()    
    Birth_Date= models.DateTimeField()
    address = models.CharField(max_length=500, default='Indore Madhya Pradesh ')
    pincode = models.IntegerField(default=0)
    city=models.CharField(max_length=200,default= 'Indore ')
    state=models.CharField(max_length=300,default='Madhya Pradesh')


class product(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE)
    Product_Name = models.CharField(max_length=50)
    Product_No = models.IntegerField()
    Product_Price=models.IntegerField()
    created_at = models.DateTimeField(default =timezone.now)
    Descreption =models.CharField(max_length=100, default=' ')
    updated_at = models.DateTimeField(default =timezone.now)
    comment =  models.CharField(max_length=100,)
    quantity = models.IntegerField(default=0)


class UserRole(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(product,on_delete=models.CASCADE,default=0)
    product_name = models.CharField(max_length=100)
    order_price  = models.FloatField()
    descreption = models.CharField(max_length=500)
    quantity = models.IntegerField(default=0)
    order_status = models.CharField(max_length=500)
    process_status =models.IntegerField(default=1)

    isactive = models.IntegerField(default=1) 



class Order( models.Model ):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    order_date = models.DateField(auto_now=True)
    amt_status = models.CharField(max_length = 200)


class comment_buyer( models.Model ):
    comment = models.CharField(max_length=800)
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    product = models.ForeignKey( product, models.CASCADE ,  related_name = 'p_comment' )

    def __str__(self):
        return self.comment



        










