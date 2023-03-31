from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Spending


# Create your views here.

def index(request):
    spendings_filter = Spending.objects.values('location').distinct()
    spendings_total = Spending.objects.aggregate(Sum('amount'))
    budget_left = 10000 - spendings_total['amount__sum']

    return render(request, 'index.html', {'spendingsfilter': spendings_filter,
                                          'spendingstotal': spendings_total,
                                          'budgetleft': budget_left})


# def spendings(request):
#     spendings_list = Spending.objects.all
#     return render(request, 'all_spendings.html', {'spendings': spendings_list})


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


# VERSION 02 - IMPROVED
class SpendingsView(generic.ListView):
    template_name = "all_spendings.html"
    context_object_name = "spendings"

    def get_queryset(self):
        return Spending.objects.all()


class SpendingDetailView(generic.DetailView):
    model = Spending
    template_name = "spending_details.html"


class SpendingCreateView(generic.CreateView):
    model = Spending
    fields = ["location", "amount", "description", "paid_with"]
    success_url = reverse_lazy("spendings:all_spendings")


def spendings(request):
    spendings_filter = Spending.objects.values('location')
    spendings_total = Spending.objects.aggregate(Sum('amount'))
    return render(request, 'all_spendings.html', {'spendingsfilter': spendings_filter,
                                                  'spendingstotal': spendings_total})
