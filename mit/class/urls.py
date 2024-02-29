from django.urls import path
from . import views


urlpatterns = [


  path('', views.home),
  path('contact/', views.contact),
  path('about/', views.about),
  path('student/', views.student),
  path('teacher/', views.teacher),
  path('insert_student/', views.insert_student)

]