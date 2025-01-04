from django.shortcuts import render
from testapp.forms import StudentForm
def student_form_view(request):
    form = StudentForm()
    return render(request,'testapp/input.html',{'form':form})
