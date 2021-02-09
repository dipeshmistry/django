from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('Contactus',views.contact,name='contact'),
    path('table',views.table,name='table')

]
