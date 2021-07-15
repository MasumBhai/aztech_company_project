from django.contrib import admin
from django.core.paginator import Paginator
from .models import *
from  django.contrib.auth.models  import  Group

admin.site.unregister(Group)

# Register your models here.

@admin.register(AboutPage)
class UserAdmin(admin.ModelAdmin):
    list_display = ['about_title','image_tag']
    list_filter = ['about_title']
    list_display_links = ['about_title']
    # radio_fields = {"goods_order_status": admin.HORIZONTAL}
    # readonly_fields = ('goods_order_id', 'buyer_id', 'goods_id', 'pub_date')
    # search_fields = ['Field1', 'Field2']
    list_per_page = 20
    paginator = Paginator
    pass

@admin.register(ContactUs)
class UserContact(admin.ModelAdmin):
    list_display = ['contact_mail','contact_time','contact_name','contact_phone','contact_msg']
    list_filter = ['contact_name']
    list_display_links = ['contact_mail']
    readonly_fields = ('contact_name','contact_mail','contact_phone','contact_time')
    list_per_page = 20
    paginator = Paginator
    # fieldsets = (
    #     (None, {
    #         'fields': ('contact_id', ('contact_name','contact_time'), ('contact_mail', 'contact_phone'),)
    #     }),
    #     ('Message left by user', {
    #         'fields': ('contact_msg',)
    #     }),
    # )
    pass