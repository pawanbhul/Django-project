from django.shortcuts import render
from .models import Student
# Create your views here.

# select * from Student
def index(request):
    students= Student.objects.all()
    context={"students":students}
        
            
    return render(request, 'index.html', context)

def home(request):
    students=["pawan","santosh","naresh"]   #list

    context={
        "students":students       #key-value pair
    }
    return render(request, 'home.html', context)