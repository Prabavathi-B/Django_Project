from django.shortcuts import  render, get_object_or_404
from django.http import HttpResponse
from .models import breakfast_details,dinner_details,juice_details,sweet_details
from django.db.models import Q



# Create your views here.
def home(request):
    return render(request,"home.html")

def recipecategory(request):
    return render(request,"recipecategory.html")

def lunch(request):
    return render(request,"lunch.html")

def breakfast_detail(request):
    query = request.GET.get('search')
    obj = breakfast_details.objects.all()

    if query:
        obj = obj.filter(Q(title__icontains=query))

    return render(request, "breakfast_detail.html", {'image': obj})

def breakfast_view(request,id):
    obj=get_object_or_404(breakfast_details, id=id)
    return render(request,'details.html',{"image":obj})


def dinner_detail(request):
    query = request.GET.get('search')
    obj = dinner_details.objects.all()

    if query:
        obj = obj.filter(Q(title__icontains=query))

    return render(request, "dinner_detail.html", {'image': obj})

def dinner_view(request,id):
    obj=get_object_or_404(dinner_details, id=id)
    return render(request,'details.html',{"image":obj})

def juice_detail(request):
    query = request.GET.get('search')
    obj = juice_details.objects.all()

    if query:
        obj = obj.filter(Q(title__icontains=query))

    return render(request, "juice_detail.html", {'image': obj})

def juice_view(request,id):
    obj=get_object_or_404(juice_details, id=id)
    return render(request,'details.html',{"image":obj})

def sweet_detail(request):
    query = request.GET.get('search')
    obj = sweet_details.objects.all()

    if query:
        obj = obj.filter(Q(title__icontains=query))

    return render(request, "sweet_detail.html", {'image': obj})


def sweet_view(request,id):
    obj=get_object_or_404(sweet_details, id=id)
    return render(request,'details.html',{"image":obj})




