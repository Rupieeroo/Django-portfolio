from django.conf.urls import url
from portfolio_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.users, name='users'),
]