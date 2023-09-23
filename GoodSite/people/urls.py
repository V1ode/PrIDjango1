from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('about/', about),
    path('pri/', pri_group),
    path('pri/<int:number_student>/', pri_id),
    path('pri/<slug:cat>/', categories),

]