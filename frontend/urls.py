from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home),
    path("showice/<id>",views.showice),
    #path("viewdetails/<id>",views.viewdetails),
    path('login',views.login),
    path('signup',views.signup),
    path('signout',views.signout),
    path('signout',views.signout),
    path('tocart',views.tocart),
    path('showcart',views.showcart),
    path('MakePayment',views.MakePayment),
    path('base1',views.base1),
    path('viewde1/<id>',views.viewde1),
    path('contact',views.contact),
    path('thank',views.thank),
    
  
]
