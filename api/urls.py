from django.urls import path

from . import views

urlpatterns = [
    path('count_class', views.counter_class),
    path('count_comment', views.counter_comment),
    path('count_file_and_folder', views.counter_file_and_folder),
    path('count_library', views.counter_library),
    path('count_line_of_code', views.counter_line_of_code),
    path('count_method', views.counter_method),
    path('count_testing', views.counter_testing),
]
