from django.urls import path
from . import views

app_name = 'spendings'

urlpatterns = [
    path("", views.index, name="index"),
    path("all_spendings/", views.SpendingsView.as_view(), name="all_spendings"),
    path("<int:pk>/", views.SpendingDetailView.as_view(), name="spending_details"),
    path("spending/", views.SpendingCreateView.as_view(), name="add"),
]
