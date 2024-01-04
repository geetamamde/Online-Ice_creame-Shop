from django.db import models

# Create your models here.


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    
    def __str__(self):
       return self.category_name
     
    class Meta :
        db_table = "Category"

class Ice_creame(models.Model):
   
    chillin_name = models.CharField(max_length=50)
    price = models.FloatField(default=50)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to="image",default="abc.jpg",null=True)
    cate = models.ForeignKey(Category,on_delete=models.CASCADE)
    

    class Meta:
        db_table ="Ice_creame"

class payment(models.Model):
    card_no = models.CharField(max_length = 10)
    cvv = models.CharField(max_length = 3)
    expiry = models.CharField(max_length = 7,default='SOME STRING')
    balance = models.FloatField(default=10000)

    class Meta:
        db_table ="payment"

