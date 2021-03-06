import random
from django.shortcuts import get_object_or_404, render
from .models import Mineral


def minerals_list(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/minerals_list.html',
                  {'minerals': minerals})


def mineral_detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/mineral_detail.html',
                  {'mineral': mineral})


def mineral_random(request):
    minerals = Mineral.objects.all()
    mineral = random.choice(minerals)
    return render(request, 'minerals/mineral_detail.html',
                  {'mineral': mineral})
