
from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
# Create your views here.
# def greet(request):
#     return HttpResponse("Hello Team")

# def greet(request):
#     return render(request,"index.html")


def greet(request):
    if request.method == 'POST':
        ename = request.POST['name'],
        eid = request.POST['id']
        edomain = request.POST['domain'],
        ecompany = request.POST['company'],
        emp = Employee(name=ename ,id=eid ,domain=edomain ,company=ecompany)
        emp.save()
    return render(request,"index.html")