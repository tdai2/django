from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=20, unique=True)
    effect = models.CharField(max_length=50)    
    type = [("A", "A"), ("P", "P"), ("F", "F")]
    skill_type = models.CharField(max_length=1, choices=type)
    proerty = [("POW", "POW"), ("TEC", "TEC"), ("STM", "STM"), ("APL", "APL"), ("SP", "SP")]
    skill_property = models.CharField(max_length=3, choices=proerty)
    pp = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    

class Ssr(models.Model):
    name = models.CharField(max_length=20, unique=True)   
    ssr_category = [("POW", "POW"), ("TEC", "TEC"), ("STM", "STM"), ("APL", "APL")] 
    type = models.CharField(max_length=3, choices=ssr_category)    
    girl = models.CharField(max_length=20)
    pow = models.IntegerField()
    tec = models.IntegerField()
    stm = models.IntegerField()
    apl = models.IntegerField()
    skill1 = models.CharField(max_length=50)
    skill2 = models.CharField(max_length=50)
    skill3 = models.CharField(max_length=50, blank=True)
    notes = models.CharField(max_length=200, blank=True)
    mod = models.BooleanField(default = False)
    Malfunction = models.BooleanField(default = False)    
    
    def __str__(self):
        return self.name
    

class Girl(models.Model):
    name = models.CharField(max_length= 20, unique=True)  
    girl_type = [("POW", "POW"), ("TEC", "TEC"), ("STM", "STM")]
    type = models.CharField(max_length=7,choices=girl_type)    
    birthday = models.DateField()
    pow = models.IntegerField()
    tec = models.IntegerField()
    stm = models.IntegerField()
    apl = models.IntegerField()
    acc_head = models.CharField(max_length=3)
    acc_face = models.CharField(max_length=3)
    acc_hand = models.CharField(max_length=3)
    
    # image
    
    def __str__(self):
        return self.name
        
class Account(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=25)
    def __str__(self):
        return self.name
    
class Ownership(models.Model):
    ssr_name = models.CharField(max_length=20)
    girl_name = models.CharField(max_length=20)  
    account_name = models.CharField(max_lenght=20)
    level = models.IntegerField(default=0)
    broken = models.BooleanField(default=False)
    