from django.shortcuts import render
import random
# Create your views here.

def home(request):
    return render(request, 'randomapp/home.html')

def result(request):

    list = ('강연우', '김서영','김소은','김유진','김정운','노은성','문다연','박경나','박혜준','오예림','이민정','이연수','장한빛','조원아','황서경')
    name = random.sample(list,1)
    return render(request, 'randomapp/result.html', {'name':name})