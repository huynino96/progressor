from django.urls import path

from . import views

urlpatterns = [
    path('language/<str:keyword>', views.language),
    path('cron', views.cron),
    path('dump', views.dump)
]
