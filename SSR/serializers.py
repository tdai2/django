from .models import Skill, Account
from rest_framework import serializers

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["name", "effect1", "effect2", "effect3", "effect4", "effect5", "effect6", "effect7", "skill_type", "skill_category", "pp"]
        
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        
