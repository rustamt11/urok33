from django.shortcuts import render
from .models import Bottle, Order, Employee, Customer, Revenue
from django.db.models import Sum
from django.utils import timezone

def dashboard(request):
    bottles = Bottle.objects.first()
    orders = Order.objects.all()
    employees = Employee.objects.all()
    customers = Customer.objects.all()


    today = timezone.now().date()
    start_of_week = today - timezone.timedelta(days=today.weekday())
    end_of_week = start_of_week + timezone.timedelta(days=6)

    start_of_month = today.replace(day=1)
    end_of_month = (start_of_month + timezone.timedelta(days=31)).replace(day=1) - timezone.timedelta(days=1)

    revenues_week = Revenue.objects.filter(date__range=[start_of_week, end_of_week]).aggregate(Sum('amount'))['amount__sum'] or 0
    revenues_month = Revenue.objects.filter(date__range=[start_of_month, end_of_month]).aggregate(Sum('amount'))['amount__sum'] or 0

    return render(request, 'app/dashboard.html', {
        'bottles': bottles,
        'orders': orders,
        'employees': employees,
        'customers': customers,
        'revenues_week': revenues_week,
        'revenues_month': revenues_month,
    })
