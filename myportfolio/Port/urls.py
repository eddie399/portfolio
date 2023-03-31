from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView, name="home"),
    path('Project/<str:pk>/', views.projectview, name="Project-page"),
    path('contact', views.contact, name="contact"),

    path('downloadFile', views.downloadFile, name="downloadFile"),

]
