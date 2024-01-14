from django.shortcuts import render, redirect
from .forms import CustomerForm, UserUpdateForm, ProfileUpdateForm, CommentForm
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .models import *


import json

from django.http import JsonResponse


# Create your views here.



# ================== Register page ======================
def register(request):
            
    # ------------------------form registration------------------------
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Created Successfully')
            return redirect('signin')
            
        
        else:
            messages.error(request, "Registration Not Successfull")
            print(form.fields)


        # if len(password) < 8:
        #     print("Make sure your password is at lest 8 letters")
        # elif re.search('[0-9]',password) is None:
        #     print("Make sure your password has a number in it")
        # elif re.search('[A-Z]',password) is None: 
        #     print("Make sure your password has a capital letter in it")
            
    else:
        form = CustomerForm()
        
    context = {'form':form}
    return render(request, 'register.html', context)



# ================== Login page ======================

def signin (request):
    
    if request.method == 'POST':
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        
        user = authenticate(request, username = username1, password = password1)
        
        if user is not None:
            login(request, user)
            print('Succeful')
            messages.success(request, 'You have Successfully Logged In')
            return redirect('dashboard')
        
        
        elif password1 != User.password or username1 != User.email :
            messages.error(request, "Invalid Username or Password")
            return redirect('signin')
        
    
    context = {}
    return render(request, 'login.html', context)


# ================= log out =================
def signout(request):
    logout(request)
    messages.success(request, 'You have Successfully Logged Out!!')
    return redirect('index')




# ================== main page ======================
def main(request):

    product = Product.objects.all()
    blog_post = Post.objects.all()

    order = None
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        
    else:
        order = None
        # return redirect('signin')
    context = {'products':product, 'order':order, 'num_of_items':0, "blog_post":blog_post}
    return render(request, 'main.html', context)


# ================== Home page ======================
def index(request):

    product = Product.objects.all()[0:9]
    package = Packages.objects.all()
    order = None
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        
    else:
        order = None
        # return redirect('signin')
    context = {'products':product, 'order':order, 'num_of_items':0, 'packages':package}
    return render(request, 'index.html', context)


# ================== gallery page ======================
def gallery(request):
    
    product = Product.objects.all()[0:9]
    order = None
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        
    else:
        order = None
        # return redirect('signin')
    context = {'products':product, 'order':order, 'num_of_items':0}
    return render(request, 'gallery.html', context)


def contact_home(request):
    order = None
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        
    else:
        order = None
        # return redirect('signin')
    context = {'order':order, 'num_of_items':0}
    return render(request, 'Contact home.html', context)

# ==================== packages page ========================
def packages(request):

    package = Packages.objects.all()
    
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)

    context = {'order':order, 'packages':package}
    return render(request, 'packages.html', context)


# ==================== packages More ========================
def packages_more(request, pk):
    package = Packages.objects.get(id = pk)

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user =request.user, complete=False)

    context = {'order':order, 'packages':package}
    return render(request, 'package_more.html', context)




# ================== Blog page ======================
def post(request):
    blog_post = Post.objects.all()
    total = Post.objects.all().count()

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        items = order.orderitem_set.all()

    context = {'blog_post':blog_post,"total":total, 'order':order}
    return render(request, 'post.html', context)


def post_details(request, pk):
    post = Post.objects.get(id = pk)

    order = None
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        items = order.orderitem_set.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect ('post_details', pk = post.id)
    else:
        form = CommentForm()

    context = {'post' : post, 'form' :form, 'items':items, 'order':order}
    return render(request, 'post_details.html', context)



# ================== Dashboard page ======================
def dashboard(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        items = order.orderitem_set.all()

    context = {'order':order, 'items':items}
    return render(request, 'dashboard.html', context)



# ==================== products page =======================
def products(request):
    product = Product.objects.all()
    
    order = None
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        items = order.orderitem_set.all()

    context = {'products':product, 'order':order, 'items':items}
    return render(request, 'product.html', context)



# ==================== services page ===================
def dash_gallery(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)

    context = {'order':order}
    return render(request, 'dash_gallery.html', context)


# ==================== contact page ===================
def contact(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)


    context = {'order':order}
    return render(request, 'contact.html', context)

# ------------------- profile page ----------------------------

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') 

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        product = Product.objects.all()
    
    
    order = None
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)

    # context = {}
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'order':order, 
    }
    return render(request, 'profile.html', context)


# ================== Add to cart JsonResponse ======================

def add_to_cart(request):
    
    data = json.loads(request.body)


    # -----------------get the product id from fetch api--------------------
    product_id = data['productid']
    action = data['action']

    # -------------------getting all product with there id--------------
    product = Product.objects.get(id=product_id)

    # ---------------------if the user is loging------------------------

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user = request.user, complete=False)
        orderitem, created = OrderItem.objects.get_or_create(order = order, product = product ) 
        items = order.orderitem_set.all()
        
        orderitem.quantity  = orderitem.quantity + 0
        if action == "add":
            orderitem.quantity = (orderitem.quantity + 1)
            
        elif action == "remove":
            orderitem.quantity = (orderitem.quantity - 1)
        orderitem.save()
        
        if orderitem.quantity <= 0:
            orderitem.delete()
        
        num_of_item = order.num_of_items
        context = {"items":items}
        
    else:
        return redirect('signin') 
    return JsonResponse(num_of_item, safe = False) 


def confirm_payment(request, pk):
    order = Order.objects.get(id=pk)
    order.complete = True
    order.save()
    messages.success(request, 'Payment made successfully!!')
    return redirect('index')



