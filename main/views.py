from django.shortcuts import render, redirect, HttpResponse

def HomePageView(request):
    template_name = 'homepage.html'
    return render(request, template_name)
