from django.contrib import admin
from django.urls import path, include
from invoiceapp.views import invoice

urlpatterns = [
    path('invoice/', invoice),

]
