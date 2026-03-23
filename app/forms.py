from django import forms
from .models import Student
# class StudentForm(forms.Form):
#     name=forms.CharField(
#         max_length=100,
#         label="Student Name",
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder':"Enter name",
#                 "class":"std_name",
#                 "id":'std-name'
#             }
#         )
#         )
#     age=forms.IntegerField()
#     marks=forms.IntegerField()
#     city=forms.CharField(max_length=100)
#     email=forms.CharField(max_length=100)

# Model Form

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields=["name", "age", "marks", "city", "email"]
        # feilds="__all__"
        widgets={
            "name":forms.TextInput(
                attrs={
                    "class": "form-control",
                    "idd": "name",
                    "placeholder": "Enter name",
                }
            )
        }

