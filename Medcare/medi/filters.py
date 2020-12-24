import django_filters
from .models import *

class DoctorFilter(django_filters.FilterSet):

    class Meta:
        model = Doctor
        fields = '__all__'
        exclude = ['phone']