from django.shortcuts import render

# Create your views here.
def index(request):
    students=[
            {"name": "pawan","age":23,"marks":80},
            {"name": "pooja","age":23,"marks":99},
            {"name": "sapana","age":21,"marks":77},
            {"name": "santosh","age":22,"marks":47},
        ]
    context={"students":students}
        
            
    return render(request, 'index.html', context)

def home(request):
    students=["pawan","santosh","naresh"]   #list

    context={
        "students":students       #key-value pair
    }
    return render(request, 'home.html', context)