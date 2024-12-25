from django.urls import path
from .views import find_answer

urlpatterns =[
    path('chat/',find_answer,name='find_answer')
]