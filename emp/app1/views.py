from django.shortcuts import render
from django.http import HttpResponse
from app1.models import employee

# Create your views here
def display(request):
    return render(request,'registration.html')
def create(request):
    if (request.method=='POST'):
        a=request.POST['emp_id']
        b=request.POST['emp_name']
        c=request.POST['salary']
        d=request.POST['place']
        e = request.FILES['img']
        v=employee.objects.create(EMPLOYEE_ID=a,EMPLOYEE_NAME=b,SALARY=c,PLACE=d,img=e)
        v.save()
        q=employee.objects.all()
        return render(request,'display.html',{'s':q})
def view(request):
    a=employee.objects.all()
    return render(request,'display.html',{'s':a})
def search(request):
    if(request.method=='POST'):
        a=request.POST['EMPLOYEE_ID']
        f=employee.objects.filter(EMPLOYEE_ID=a)
    return render(request,'display.html',{'s':f})
def delete(request):
    if (request.method=="POST"):
        a=request.POST['emp_id']
        data=employee.objects.filter(EMPLOYEE_ID=a)
        data.delete()
        r=employee.objects.all()
        return render(request, 'display.html', {'s':r})
        #return HttpResponse("Deleted")