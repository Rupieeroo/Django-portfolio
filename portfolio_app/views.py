from django.shortcuts import render
from portfolio_app.models import User


def index(request):
    return render(request, 'portfolio_app/index.html')