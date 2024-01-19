from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Employee

# Create your views here.
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    context = {
        "employee": employee
    }
    return render(request, "employee_detail.html", context)
    
    # try:
    #     employee = Employee.objects.get(id=pk)
    # except:
    #     raise Http404

