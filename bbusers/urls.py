from django.urls import path
from . import views


urlpatterns = [
  path('', views.BbUserListView.as_view(), name='create_users'),

]

