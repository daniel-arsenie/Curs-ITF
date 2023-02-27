from django.urls import path
from . import views

app_name = 'spendings'

urlpatterns = [
    path('', views.spendings, name='all_spendings'),
    path('<int:spending_id>/', views.spending_detail, name='spending_details'),
    path('spending/', views.spending_add, name='add')
]
