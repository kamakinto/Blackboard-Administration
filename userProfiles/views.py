from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class UserProfileView(LoginRequiredMixin, TemplateView):
  template_name = 'profile.html'
  login_url = '/users/login/'
