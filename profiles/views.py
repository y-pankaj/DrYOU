from django.utils import timezone
from django.shortcuts import render, get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required



def ProfileView(request):
    return  render(request, 'Profilepage.html')