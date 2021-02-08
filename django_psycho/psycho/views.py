from django.shortcuts import render, get_object_or_404
from .models import PsychoMaster, Method, RawMethod, RawData
from .serializers import PsychoMasterSerializer, PsychoMasterDetailSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView


def start(request):
    ctx = {
        'psychologistic': PsychoMaster.objects.all(),
        # 'image': f'media/{PsychoMaster.objects.all()}'
        # 'methods': Method.objects.get(PsychoMaster),
        'test_methods': Method.objects.all(),
    }
    return render(request, 'index.html', context=ctx)


class PsychoMastersList(ListAPIView):
    serializer_class = PsychoMasterSerializer
    queryset = PsychoMaster.objects


class PsychoMastersDetail(RetrieveAPIView):
    serializer_class = PsychoMasterDetailSerializer

    def get_queryset(self):
        return PsychoMaster.objects.all()


