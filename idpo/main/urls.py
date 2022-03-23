from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('course/<int:id>', views.course, name='course'),
    path('news/<int:id>', views.news, name='news'),



]
