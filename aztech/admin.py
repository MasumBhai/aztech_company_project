from django.contrib import admin
from django.core.paginator import Paginator

from .models import *
# Register your models here.
# admin.site.register(about)
@admin.register(aboutpage)
class UserAdmin(admin.ModelAdmin):
    list_display = ['about_title']
    list_filter = ['about_title']
    list_display_links = ['about_title']
    # radio_fields = {"goods_order_status": admin.HORIZONTAL}
    # readonly_fields = ('goods_order_id', 'buyer_id', 'goods_id', 'pub_date')
    # search_fields = ['Field1', 'Field2']
    list_per_page = 20
    paginator = Paginator
    pass
