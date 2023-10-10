from django.contrib import admin
from .models import Restaurant,menucategory,menuitem,Accounts

# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id','Restaurant_name','Restaurant_city','Restaurant_contact_no','image']

class menuitemadmin(admin.ModelAdmin):
    list_display = ['id','name','price','cat_fk','image']

class menucategoryadmin(admin.ModelAdmin):
    list_display = ['id','name']

class AccountsAdmin(admin.ModelAdmin):
    list_display = ['cardno','cvv','expiry','balance']


admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(menuitem,menuitemadmin)
admin.site.register(menucategory,menucategoryadmin)
admin.site.register(Accounts,AccountsAdmin)


