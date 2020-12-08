from django.urls import path
from authentication import views
from django.conf.urls import url
urlpatterns = [

    #path('form/', views.call_form),
    path('signup', views.signup,name='signup'),
    path('login/<int:prize>', views.login,name='login'),
    url('verify',views.verify,name='verify'),
    path('generate',views.generate,name="generate"),
    path('change_pass',views.change_pass,name='change_pass'),
    path('show',views.show),
    path('payment/<int:prize>',views.payment,name='payment'),
    
]
    