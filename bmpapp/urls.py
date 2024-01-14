
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    # ======================== index and main =======================
    path('main', views.main, name='main'),
    path('', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact_home/', views.contact_home, name='contact_home'),

        # ======================== register =======================
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    
    
    # ======================== dashboard =======================
    path('dashboard', views.dashboard, name='dashboard'),
    path('products/', views.products, name='products'),
    path('dash_gallery/', views.dash_gallery, name='dash_gallery'),
    path('packages/', views.packages, name='packages'),
    
    # ======================== contact and profile =======================
    path('contact/', views.contact, name='contact'),
    path('profile', views.profile, name='profile'),
    
    
    # ======================== Json Response =======================
    path('add_to_cart', views.add_to_cart, name=''),


    # ============================ Blog Page ===========================



    path('post/', views.post, name="post"),

    path('<str:pk>/', views.post_details, name='post_details'),

    path('packages_more/<str:pk>', views.packages_more, name='packages_more'),
    
    path('confirm_pay/<str:pk>', views.confirm_payment, name='add'),

    
    

    

]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
