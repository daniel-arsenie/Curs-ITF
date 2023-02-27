from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Spending


# Create your views here.

def index(request):
    return HttpResponse('Hello world, Here is Spendings index.')


def spendings(request):
    spendings_list = Spending.objects.all
    return render(request, 'all_spendings.html', {'spendings': spendings_list})


def spending_detail(request, spending_id):
    spending = get_object_or_404(Spending, pk=spending_id)
    return render(request, 'spending_details.html', {'spending': spending})

def spending_add(request):
    spending_data = request.POST.dict()
    try:
        spending = Spending(
            location=spending_data['location'],
            amount=spending_data['amount'],
            description=spending_data['description'],
            paid_with=spending_data['paid_with'],
        )
        spending.save()
    except KeyError:
        return render(request, 'error.html', {'error_message': 'Error! Invalid spending details!'})
    return HttpResponseRedirect(reverse('spendings:all_spendings'))
