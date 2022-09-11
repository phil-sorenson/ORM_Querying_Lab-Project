from django.urls import path
from . import views


app_name = 'lab'
urlpatterns = [
    path('', views.example_solution, name="index"),
    path('one/', views.problem_one, name="one"),
    path('two/', views.problem_two, name="two"),
    path('three/', views.problem_three, name="three"),
    path('four/', views.problem_four, name="four"),
    path('five/', views.problem_five, name="five"),
    path('six/', views.problem_six, name="six"),
    path('seven/', views.problem_seven, name="seven"),
    path('bonus/', views.bonus_problem, name="bonus")
]