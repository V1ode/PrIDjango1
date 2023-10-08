from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('pri/', pri_group),
    path('pri/<int:number_student>/', pri_id, name='spisok_pri'),
    path('pri/<slug:cat>/', categories, name='categories'),
    path('<int:year>/', date_handler, name='date_handler'),
    path('home/', redirect_to_home, name='home_redirect'),
    path('Eugen/', redirect_to_Eugen, name='Eugen_redirect'),
]