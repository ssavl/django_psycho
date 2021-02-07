from django.shortcuts import render, get_object_or_404
from .models import PsychoMaster, Method, RawMethod, RawData


def start(request):
    ctx = {
        'psychologistic': PsychoMaster.objects.all(),
        # 'image': f'media/{PsychoMaster.objects.all()}'
        # 'methods': Method.objects.get(PsychoMaster),
        'test_methods': Method.objects.all(),
    }
    return render(request, 'index.html', context=ctx)