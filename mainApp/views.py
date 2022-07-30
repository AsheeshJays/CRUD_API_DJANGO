from django.shortcuts import render, HttpResponseRedirect
from .models import Employee
from .forms import EmployeeForm


def IndexPage(request):
    if request.method == 'POST':
        fm = EmployeeForm(request.POST)
        if fm.is_valid():
            empID = fm.cleaned_data['empID']
            empName = fm.cleaned_data['empName']
            empDesgination = fm.cleaned_data['empDesgination']
            empSalary = fm.cleaned_data['empSalary']
            reg = Employee( empID=empID,empName=empName,empDesgination=empDesgination,empSalary=empSalary)
            fm.save()
    else:
        fm = EmployeeForm()
    emp = Employee.objects.all()
    return render(request, 'index.html',{'form':fm,'emp':emp})

def delete_data(request, id):
    if request.method == 'POST':
        pi = Employee.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update_data(request , id):
    pi = Employee.objects.get(pk=id)
    fm = EmployeeForm(request.POST, instance=pi)
    if fm.is_valid():
        fm.save()
    else:
        pi = Employee.objects.get(pk=id)
        fm = EmployeeForm(instance=pi)
    return render(request, 'update.html',{'form':fm})