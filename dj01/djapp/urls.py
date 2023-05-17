from django.urls import path
from .views import student_list
from .views import Courses_list

urlpatterns = [
    path('students/',student_list),
    path('courses/',Courses_list),
]
