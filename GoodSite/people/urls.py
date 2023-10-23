from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('object_types/', object_types, name='object_types'),
    path('about/', about, name='about'),
    path('test_split_line/<str:line>/<str:sep>/', test_split_line, name='Split_line Tester'),
    path('pri/', pri_group),
    path('pri/<int:number_student>/', pri_id, name='spisok_pri'),
    path('pri/<slug:cat>/', categories, name='categories'),
    path('<int:year>/', date_handler, name='date_handler'),
    path('post/', post_detail, name="post_detail"),
    path('home/', redirect_to_home, name='home_redirect'),
    path('<str:name>/', redirect_to_Eugen, name='Eugen_redirect'),
]