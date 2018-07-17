from django.shortcuts import render
from django.template import loader
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    template = loader.get_template("main/index.html")
    return render(request, 'main/index.html')

@login_required
def get_user_profile(request,username):
    user = User.objects.get(username=username)
    #return render(request, 'uploads')
