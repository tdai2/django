from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=10)
    effect1 = models.CharField(max_length=30)
    effect2 = models.CharField(max_length=30, blank = True)
    effect3 = models.CharField(max_length=30, blank = True)
    effect4 = models.CharField(max_length=30, blank = True)
    effect5 = models.CharField(max_length=30, blank = True)
    effect6 = models.CharField(max_length=30, blank = True)
    effect7 = models.CharField(max_length=30, blank = True)
    
    type = [("A", "A"), ("P", "P"), ("F", "F")]
    skill_type = models.CharField(max_length=1, choices=type)
    
    category = [("POW", "POW"), ("TEC", "TEC"), ("STM", "STM"), ("APL", "APL"), ("SP", "SP")]
    skill_category = models.CharField(max_length=3, choices=category)
    pp = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    

class Ssr(models.Model):
    name = models.CharField(max_length=10)   
    ssr_category = [("POW", "POW"), ("TEC", "TEC"), ("STM", "STM"), ("APL", "APL")] 
    type = models.CharField(max_length=3, choices=ssr_category)    
    girl = models.ForeignKey("Girl", on_delete=models.CASCADE, related_name='girl')
    skill_1 = models.ForeignKey("Skill", on_delete=models.CASCADE, related_name='skill1')
    skill_2 = models.ForeignKey("Skill", on_delete=models.CASCADE, related_name='skill2')
    skill_3 = models.ForeignKey("Skill", on_delete=models.CASCADE, related_name='skill3')
    mod = models.BooleanField(default = False)
    Malfunction = models.BooleanField(default = False)    
    
    def __str__(self):
        return self.name
    

class Girl(models.Model):
    name = models.CharField(max_length= 5)  
    girl_type = [("POW", "POW"), ("TEC", "TEC"), ("STM+POW", "STM+POW"), ("STM+TEC", "STM+TEC")]
    type = models.CharField(max_length=7,choices=girl_type)
    birthday = models.DateField()
    # image
    
    def __str__(self):
        return self.name
    
    
    
class Account(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=25)
    # [{"girl_nane":"name","girl_level":0, "girl_photo_level":0, "girl_relationship":["girl_name":0], "a_skill_list":[], "cheer_board_list":[] }]
    girls_detail = models.JSONField(blank=True)
    # [{"ssr_id" : "SSR_id", "SSR_level" : 0}]
    ssrs_detail = models.JSONField(blank=True)
    
    def __str__(self):
        return self.name
    
  