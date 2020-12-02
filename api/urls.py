from django.urls import path

from . import views

urlpatterns = [
    path('count_class/<str:author>/<str:repository>', views.counter_class),
    path('count_class/<str:author>/<str:repository>/create', views.create_counter_class),

    path('count_file_and_folder/<str:author>/<str:repository>', views.counter_file_and_folder),
    path('count_file_and_folder/<str:author>/<str:repository>/create', views.create_counter_file_and_folder),

    path('count_comment/<str:author>/<str:repository>', views.counter_comment),
    path('count_comment/<str:author>/<str:repository>/create', views.create_counter_comment),

    path('count_library/<str:author>/<str:repository>', views.counter_library),
    path('count_library/<str:author>/<str:repository>/create', views.create_counter_library),
    
    path('count_line_of_code/<str:author>/<str:repository>', views.counter_loc),
    path('count_line_of_code/<str:author>/<str:repository>/create', views.create_counter_loc),
    
    path('count_method/<str:author>/<str:repository>', views.counter_method),
    path('count_method/<str:author>/<str:repository>/create', views.create_counter_method),

    path('count_testing/<str:author>/<str:repository>', views.counter_testing),
    path('count_testing/<str:author>/<str:repository>/create', views.create_counter_testing),
]
