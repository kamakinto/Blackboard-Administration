from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import requests

class BBAdminView(LoginRequiredMixin, TemplateView):
  template_name = 'bbadmin.html'
  login_url='/users/login/'

  def get(self, request):
    # template_name = 'bbadmin.html'
    # username='958ce421-1453-42a6-973c-15ba6cc49c72'
    # secret='dSG8xaI1hnVlR5538C2Y8Hegc6Sezzzu'
    # curlData='grant_type=client_credentials'
    # header = {'Content-type': 'application/x-www-form-urlencoded'}
    # bbAuthAddress = 'https://blackboard.aup.edu/learn/api/public/v1/oauth2/token'
    # response = requests.post('https://blackboard.aup.edu/learn/api/public/v1/oauth2/token', auth=('958ce421-1453-42a6-973c-15ba6cc49c72', 'dSG8xaI1hnVlR5538C2Y8Hegc6Sezzzu'), headers = header, data= 'grant_type=client_credentials')
    # jsonResponse = response.json()
    # print(response.json())
    #logic

    return render(request, 'bbadmin.html', {
      # 'access_token': jsonResponse['access_token'],
      # 'expiration_time': jsonResponse['expires_in']
       'access_token': 249802394032,
       'expiration_time': '1 hour'
    })





# Create your views here.
