from django.shortcuts import render
from college.models import destination
from django.db.models import Q

# Create your views here.

def college_info(request):
    student = destination.objects.all()
    return render(request,'index.html',{'student':student})


def college_details(request,pk):
    student = destination.objects.get(pk=pk)
    return render(request,'index1.html',{'student':student})


def college_info1(request):
    student = destination.objects.all().values()
    return render(request,'index2.html',{'student':student})


def college_info2(request):
    student = destination.objects.all().values_list('Firstname')
    return render(request,'index3.html',{'student':student})

def college_info3(request):
    student = destination.objects.filter(Firstname = 'Priya').values()
    return render(request,'index4.html',{'student':student})

def college_info4(request):
    student = destination.objects.filter(Lastname = 'L',id = 4).values()
    return render(request,'index5.html',{'student':student})

def college_info5(request):
    student = destination.objects.filter(Firstname='Madhu').values() | destination.objects.filter(Firstname='Elan').values()
    return render(request,'index6.html',{'student':student})

def college_info6(request):
    student = destination.objects.filter(Q(Firstname='Dharani') |  Q(Firstname='Janani')).values()
    return render(request,'index7.html',{'student':student})

def college_info7(request):
    student = destination.objects.filter(Firstname__startswith='J').values()
    return render(request,'index7.html',{'student':student})

def college_info8(request):
    student = destination.objects.all().order_by('Firstname').values()
    return render(request,'index7.html',{'student':student})

def college_info9(request):
    student = destination.objects.all().order_by('-Firstname').values()
    return render(request,'index7.html',{'student':student})

def college_info10(request):
    student = destination.objects.all().order_by('Lastname', '-id').values()
    return render(request,'index7.html',{'student':student})


