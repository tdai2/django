from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=10)
    effect1 = models.CharField(max_length=30)
    effect2 = models.CharField(max_length=30)
    effect3 = models.CharField(max_length=30)
    effect4 = models.CharField(max_length=30)
    effect5 = models.CharField(max_length=30)
    type = models.CharField(max_length=2)
    pp = models.IntegerField(default=0)
    

class Ssr(models.Model):
    name = models.CharField(max_length=10)    
    type = models.CharField(max_length=5)
    girls = models.JSONField()
    skill_1 = models.ForeignKey("Skill", on_delete=models.CASCADE, related_name='skill1')
    skill_2 = models.ForeignKey("Skill", on_delete=models.CASCADE, related_name='skill2')
    skill_3 = models.ForeignKey("Skill", on_delete=models.CASCADE, related_name='skill3')
    mod = models.BooleanField(default = False)
    Malfunction = models.BooleanField(default = False)    
    

class Girl(models.Model):
    name = models.CharField(max_length= 5)
    # level = models.IntegerField(default=1)
    type = models.CharField(max_length=3)
    # photo_level = models.IntegerField(default=1) 
    # def ssr_detail():
    #     return {}       
    # ssrs_detail = models.JSONField(default=ssr_detail)
    
class Account(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    girls_detail = models.JSONField()
    
    
    
    

    

   
    
