from .models import Skill, Account, Girl, Ssr
from rest_framework import serializers

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class SsrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ssr
        fields = '__all__'
        
class GirlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Girl
        fields = '__all__'
        
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        
