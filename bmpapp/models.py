from django.db import models
from PIL import Image

from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}' #show how we want it to be displayed
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        
        if img.width > 300 or img.height > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path) 
            
    
    
            
class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
        
    
    
class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True, default=None)
    
    def __str__(self):
        return str(self.id)
    
    
    # --------------------getting the sum of all the items total price of a products --------------------
    @property
    def total_item_price(self):
        order_items = self.orderitem_set.all()
        total = sum([item.item_total_price for item in order_items])
        return total
    
    # ------------------------ getting the sum of all the quantity of products ----------------------------
    @property
    def num_of_items(self):
        order_items = self.orderitem_set.all()
        quantity_total = sum([item.quantity for item in order_items])
        return quantity_total
    
    
    
    
# ---------------OrderItem are the Items in our cart--------------------
class OrderItem(models.Model):
     # ----------a cart can have many order item in it----------------
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity  = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    
    # ---------------------getting total for a particular product ordered-----------------
    @property
    def item_total_price(self):
        new_price = self.product.price * self.quantity
        return new_price
    


class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200)
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
    
    @property
    def imageURL2(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class Commments(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete= models.CASCADE)
    users = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    date_addded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
    
    

class Packages(models.Model):
    images = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
        
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL3(self):
        try:
            url = self.images.url
        except:
            url = ''
        return url
    

    # @property
    def desc_arr(self):
        try:
            descri_work = self.description.split("###")
        except:
            descri_work = ""
        return descri_work
    

        



    
    