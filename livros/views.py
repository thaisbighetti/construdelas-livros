from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from livros.models import Livro


def index(request):
    if request.method == "GET":
        return render(request, "index.html")


def usuario_login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        usuario = authenticate(
            username=request.POST.get("username"), password=request.POST.get("password")
        )
        if usuario is not None:
            login(request, usuario)
            return redirect("livros")
        else:
            return HttpResponse("USUARIO NÃO EXISTE")


def criar_usuario(request):
    if request.method == "GET":
        return render(request, "criar_usuario.html")
    elif request.method == "POST":
        with transaction.atomic():
            User.objects.create_user(
                password=request.POST.get("password"),
                email=request.POST.get("email"),
                username=request.POST.get("username"),
            )
            return redirect("livros")


@login_required(login_url="http://127.0.0.1:8000/login/")
def livro_detail(request, *args, **kwargs):
    if request.method == "GET":
        livros = Livro.objects.all()
        return render(request, "livros.html", {"livros": livros})
    elif request.method == "POST":
        with transaction.atomic():
            print(request.POST)
            Livro.objects.create(
                titulo=request.POST.get("titulo"),
                numero_de_paginas=request.POST.get("numero_paginas"),
                editora=request.POST.get("editora"),
            )
            return redirect("livros")
