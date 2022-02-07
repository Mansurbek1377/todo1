from django.shortcuts import render
from .models import TODO, Day


def index(request):
    return render(request, 'todo/index.html')


def home(request):
    days_of_the_week = Day.objects.all()
    return render(request, 'todo/home.html', {'days_of_the_week': days_of_the_week})


def concrete_plan(request, plan_id):
    plan = Day.objects.get(id=plan_id)
    concrete_plan1 = plan.todo_set.all()
    return render(request, 'todo/plan.html', {'concrete_plan1': concrete_plan1, 'plan':plan })