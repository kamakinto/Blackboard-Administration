from django.urls import path
from . import views

urlpatterns = [
  path('', views.BBAdminView.as_view(), name='bbadmin'),
  path('create_course/', views.BBAdminView.as_view(), name='create_course'),

]