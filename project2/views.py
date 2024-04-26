from django.shortcuts import render
from django.http import HttpResponse
from urllib import request
from string import punctuation


def index(request):
    return render(request,"textutils.html")

def removepunccation(request):
    input = request.GET.get('text','default')
    removepunccation = request.GET.get('removepunccation','off')
    capalitize = request.GET.get('capalitize','off')

    if removepunccation=='on':
        punctuation = """!@#$%&*(){}[]?><:;"""
        analyze = " "
        for char in input:
            if char not in punctuation:
                analyze = analyze+char

        user_input = {'Task':'Remove Puncation','analyzed_text': analyze}
        return render(request,'analyze.html',user_input) 


    elif capalitize=='on':
        analyze = " "

        for char in input:
            analyze+=char.upper()

        user_input = {'Task':'Capatalized','analyzed_text': analyze}
        return render(request,'analyze.html',user_input)   

    else:
        return HttpResponse("Error - Your Text Has Not Been Analyzed ")
    

# def capalitize(request):






# def spaceremover(request):
#     return HttpResponse()

def home(request):
    return HttpResponse("Welcome to the Home Page of the website")
