from django.contrib import admin


from .models import *
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Commments)
admin.site.register(Packages)