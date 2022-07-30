from dataclasses import fields
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {
            'empID':forms.TextInput(attrs={'class':'form-control'}),
            'empName':forms.TextInput(attrs={'class':'form-control'}),
            'empDesgination':forms.TextInput(attrs={'class':'form-control'}),
            'empSalary':forms.TextInput(attrs={'class':'form-control'}),
        }