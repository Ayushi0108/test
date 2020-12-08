from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('contact/', views.contact, name='contact'),
    url(r'^delete/(?P<email>.+?)/$', views.delete_contact, name="delete_contact"),
    path('terms_conditions/',views.terms_conditions, name="terms-conditions"),
    path('privacy_policy/',views.privacy_policy, name="privacy-policy"),
    path('customers/',views.customers,name='customers'),
    path('logout/',views.logout,name='logout'),
    path('inbox/', views.inbox, name='inbox'),
]
