from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import CarForm
from .models import Car


def cars_views(request):
    cars_list = Car.objects.all().order_by('model')
    search = request.GET.get('search')

    if search:
        cars_list = cars_list.filter(model__icontains=search)

    paginator = Paginator(cars_list, 10)
    page_number = request.GET.get('page')
    cars = paginator.get_page(page_number)

    context = {'cars': cars}

    return render(
        request,
        'cars.html',
        context=context
    )


def car_create_view(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cars')
    else:
        form = CarForm()

    return render(request, 'new_car.html', {'form': form})
