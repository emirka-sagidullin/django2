from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hiip(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    ip = request.META['REMOTE_ADDR']

    return HttpResponse(f"""
        <p>Host: {host}</p>
        <p>Info: {user_agent}</p>
        <p>IP: {ip}</p>
    """)

def error(request):
    return HttpResponse("К сожалению, произошла ошибка", status=400, reason='Djavapon')

def user(request, login='Javapon', folder='Djangopon', num_of_folder=0):
    return HttpResponse(f"""
        <p>Login: {login}</p>
        <p>Folder: {folder}</p>
        <p>Num of folder: {num_of_folder}</p>
    """)