from django.urls import path
from . import views 

urlpatterns =[
    path('',views.Mainpage),
    path('menu/<int:id1>',views.menu),
    path('signup',views.signup),
    path('login',views.login),
    path('logout',views.logout),
    path('showcart',views.showcart),
    path('addtocart',views.addtocart),
    path('modifycart',views.modifycart),
    path('makepayment',views.makepayment),
    path('about',views.about),
    path('contact',views.contact),
    path('savedetails',views.savedetails),
]