from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","price", "category", "brand", "stock", "labels")
    list_filter = ('category','brand','stock','labels')
    search_fields = ('name','description')





admin.site.register(Category)
admin.site.register(Slider)
admin.site.register(ADD)
admin.site.register(Brand)
# admin.site.register(Feedback)
admin.site.register(StieInfo)
# admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(ProductReviews)




