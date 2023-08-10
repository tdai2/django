from django.shortcuts import render
from django.http import HttpResponse
from .models import Account, Ssr, Skill, Girl
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import SkillSerializer, AccountSerializer, SsrSerializer, GirlSerializer

def home(request):
    return HttpResponse("Hello, Django!")

# Create your views here.
class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    # permission_classes = [permissions.IsAuthenticated]

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
class SsrViewSet(viewsets.ModelViewSet):
    queryset = Ssr.objects.all()
    serializer_class = SsrSerializer
    
class GirlViewSet(viewsets.ModelViewSet):
    queryset = Girl.objects.all()
    serializer_class = GirlSerializer
