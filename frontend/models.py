from django.db import models
from backend.models import Ice_creame
from datetime import datetime

class userinfo(models.Model):
    username = models.CharField(max_length=20 ,primary_key=True)
    fname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.IntegerField()

    class Meta:
        db_table = "userinfo"


class mycart(models.Model):
    user = models.ForeignKey(userinfo,on_delete=models.CASCADE)
    ice_creame = models.ForeignKey(Ice_creame,on_delete=models.CASCADE,default = None)
    qty = models.IntegerField(default=1)

    class Meta:
        db_table = "mycart"


class OrderMaster(models.Model):
     user = models.ForeignKey(userinfo,on_delete=models.CASCADE)
     date_of_order = models.DateField(default=datetime.now)
     amount = models.FloatField(default = 100000)
     details = models.CharField(max_length =200)

     class Meta:
         db_table = "OrderMaster"

class Contact_info(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    subject = models.CharField(max_length=500)

    
    class Meta:
         db_table = "Contact_info"

       







