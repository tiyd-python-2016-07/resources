from django.shortcuts import render
from .models import Ability
from .serializers import AbilitySerializer
from rest_framework import viewsets


def index(request):
    return render(request, 'index.html')


class AbilityViewSet(viewsets.ModelViewSet):
    serializer_class = AbilitySerializer
    queryset = Ability.objects.all().order_by('name')
