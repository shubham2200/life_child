from django.contrib import admin
from .models import Raise_user  ,Donate_fund
# Register your models here.
class Raise_Admin(admin.ModelAdmin):
    list_display = ('id', 'name' ,'email' , 'date')


class Donate_admin(admin.ModelAdmin):
    list_display = ( 'full_name' , 'email' , 'city', 'amount')

admin.site.register( Raise_user , Raise_Admin )
admin.site.register( Donate_fund , Donate_admin)