from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from xxx_api import views

urlpatterns = [
    path("v1/", views.DoBackground.as_view()),
]
