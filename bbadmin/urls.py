from django.urls import path
from . import views

urlpatterns = [
  path('', views.BBAdminView.as_view(), name='bbadmin'),
]