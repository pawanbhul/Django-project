from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# Create your views here.

def home(request):

    # Fetches all record
    students = Student.objects.all()

    # Fetches single record
    # student_1 = Student.objects.get(id=1)

    # Fetches students with marks > 40. Filter condition: lt,gt,lte,gte
    # students_marks = Student.objects.filter(marks__gt=80)

    # Create new record(INSERT)

    # Student.objects.create(
    #     name="Gita",
    #     age=22,
    #     marks=64,
    #     city="Kathmandu",
    #     email="gita1@gmail.com",
    #     is_active=False
    # )

    # Update student record
    # student_update = Student.objects.get(id=2)
    # student_update.marks = 90
    # student_update.city = "Kathmandu"
    # student_update.save()

    #Delete student record
    # student_delete = Student.objects.get(id=6)
    # student_delete.delete()

    context = {
        "students": students,
        # "student_1":student_1,
        # "students_marks":students_marks
        }

    return render(request, "home.html", context)

# def student_form(request):
#     if request.method == "POST":
#         name=request.POST.get("name")
#         age=request.POST.get("age")
#         marks=request.POST.get("marks")
#         city=request.POST.get("city")
#         email=request.POST.get("email")

#         Student.objects.create(
#             name=name,
#             age=age,
#             marks=marks,
#             city=city,
#             email=email
#         )

#         return redirect("home")

#     return render(request, "form.html")


def Student_form(request):

    if request.method == "POST":
        form=StudentForm(request.POST)

        if form.is_valid():
            data=form.cleaned_data
            print(data)
            Student.objects.create(
                name=data["name"],
                age=data["age"],
                marks=data["marks"],
                city=data["city"],
                email=data["email"],
        
            )
            return redirect("home")


    else:
        form = StudentForm()

    context={"form":form}
    return render(request,"form.html", context)


def update_student(request, id):
    student= get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = StudentForm(instance=student)

    context = {"form": form}
    return render(request, "form.html", context)

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("home")