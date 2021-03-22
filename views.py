from django.shortcuts import render, HttpResponse
from home import urls
from .models import *
# Create your views here.
def index(request):
    content = {}
    info = Student.objects
    content['name'] = info
    content['context'] = "Hello again"
    print(info.all)
    return render(request,'index.html', content)
