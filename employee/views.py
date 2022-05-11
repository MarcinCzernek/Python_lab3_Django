from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.contrib import messages

from employee.forms import EmployeeForm
from employee.models import Employee
from django.shortcuts import render, redirect

@login_required(login_url='/login/')
def displaydata(request):
    results = Employee.objects.all()
    return render(request,"employee/index.html",{"Employee":results})

def editemp(request,id):
    displayemp=Employee.objects.get(id=id)
    return render(request,"employee/edit.html",{"employee":displayemp})

def updateemp(request,id):
    updateemp= Employee.objects.get(id=id)
    form=EmployeeForm(request.POST, instance=updateemp)
    if form.is_valid:
        form.save()
        messages.success(request,"Record Updated Successfully...!")
        return render(request,"employee/edit.html",{"employee":updateemp})

def deleteemp(request,id):
    deleteemployee=Employee.objects.get(id=id)
    deleteemployee.delete()
    result=Employee.objects.all()
    return render(request,'employee/index.html',{"Employee":result})

@login_required(login_url='/login/')
def addemp(request):
    if request.method == 'POST':
        employee = EmployeeForm(request.POST)
        if employee.is_valid():
            employee = employee.save(commit=False)
            employee.save()
            return redirect('displaydata')
        else:
            context = {'form': employee}
            return render(request, 'employee/add.html', context)
    else:
        employee = EmployeeForm()
        context = {'form': employee}
        return render(request, 'employee/add.html', context)




