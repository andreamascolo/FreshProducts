from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm
from .forms import LoginForm


# Create your views here.
def index(request):
    templates = loader.get_template('Homepage.html')
    return HttpResponse(templates.render())
    #return HttpResponse("Hello, world. You're at the FreshProducts index.")
'''modfiche effettuate h 17.47'''
def login(request):
    username = 'not logged in'
   
    if request.method == 'POST':
        MyLoginForm = LoginForm(request.POST)
      
    if MyLoginForm.is_valid():
        username = MyLoginForm.cleaned_data['username']
        request.session['username'] = username
    else:
        MyLoginForm = LoginForm()
			
    return render(request, 'loggedin.html', {"username" : username})

def formView(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'loggedin.html', {"username" : username})
    else:
        return render(request, 'login.html', {})

'''
def login(request):
    templates = loader.get_template('Login.html')
    return HttpResponse(templates.render())
    #return HttpResponse("Hello, world. You're at the FreshProducts index.")
'''


def registrer(request):
    templates = loader.get_template('Registrer.html')
    return HttpResponse(templates.render())
    #return HttpResponse("Hello, world. You're at the FreshProducts index.")

def contact(request):
    templates = loader.get_template('Contact.html')
    return HttpResponse(templates.render())
    #return HttpResponse("Hello, world. You're at the FreshProducts index.")

def area_riservata(request):
    templates = loader.get_template('Area_riservata.html')
    return HttpResponse(templates.render())
    #return HttpResponse("Hello, world. You're at the FreshProducts index.")