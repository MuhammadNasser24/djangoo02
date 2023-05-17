from django.shortcuts import render



# Create your views here.
from .models import Students_models1
from .models import Courses

def student_list(request):
    student_details = Students_models1.objects.all()
    return render(request,'students.html',{'std':student_details})


def Courses_list(request):
    courses_details = Courses.objects.all()
    return render(request,'courses.html',{'crs':courses_details})