from django.shortcuts import render , redirect
from .forms import StudentForm
# Create your views here. logic part

def index(request):
    return render(request, 'student/index.html')

# def student_page(request):
#     return render(request,'student/student.html')

## ?  view kısmı logic kısmı dedik. burada yaptıgımız değişiklikleri urls.py ya tanıtmak lazım. models yapılan değişikliği adminde tanıtmak gibi

# def student_page(request):
#     form = StudentForm()
#     context = {
#         "form" : form
#      }
#     return render(request , "student/student.html" , context)


def student_page(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST , request.FILES)
    if form.is_valid():
        form.save()
        return redirect("student")
    
    context = {
        "form" : form
    }
    return render (request , "student/student.html" , context)