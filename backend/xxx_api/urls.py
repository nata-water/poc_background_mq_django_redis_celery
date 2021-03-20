from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from xxx_api import views

urlpatterns = [
    path("v1/", views.DoBackground.as_view()),
    path("v1/do_parse_resource/", views.ResourceControl.as_view()),
    # path("v1/resource_spec/", views.ResourceSpec.as_view()),
]
