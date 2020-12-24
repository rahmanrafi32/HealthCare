from django.shortcuts import render
from .models import *
from .filters import DoctorFilter

# Create your views here.
def index(request):
    return render(request, "index.html")

def doctors(request):
    doctors = Doctor.objects.all()

    myFilter = DoctorFilter(request.GET, queryset = doctors)
    doctors = myFilter.qs

    context = {'doctors': doctors, 'myFilter': myFilter}
    return render(request, "doctorlist.html", context)

