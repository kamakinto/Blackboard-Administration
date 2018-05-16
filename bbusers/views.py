from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BbUser
import services
import pprint
# Create your views here.

class BbUserListView(LoginRequiredMixin, TemplateView):
  template_name = 'createUsers.html'
  login_url='/users/login/'



  def get(self, request):
    bbUsers = BbUser.objects.all()
    return render(request, 'createUsers.html', {
       'user_list': bbUsers
     })

     #post method for form data
  def post(self, request):
    userDictList = services.getUserDictList(request)
    #send userDictList to background task for processing into a user list
    

    pprint.pprint(userDictList)

    return render(request, 'createUsers.html')



