from django.contrib import admin
from .models import Ice_creame,Category,payment


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display =("id", "category_name")

class Ice_creameAdmin(admin.ModelAdmin):
    list_display=("id","chillin_name","price", "description","image","cate")

class paymentAdmin(admin.ModelAdmin):
    list_display=("id","card_no","cvv","expiry")




admin.site.register(Category, CategoryAdmin)
admin.site.register(Ice_creame,Ice_creameAdmin)
admin.site.register(payment,paymentAdmin)
