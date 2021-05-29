from django.db import models

# Create your models here.

class Member(models.Model):
    phone = models.CharField(max_length=11)
    name = models.CharField(max_length=30)
    points = models.IntegerField(default=0)
    password = models.CharField(max_length=30, null=True )
    def __str__(self):
        return self.name


class Discharge(models.Model):
    discharge_date = models.DateField()
    material = models.CharField(max_length=10)
    machine_id = models.IntegerField()
    who = models.ForeignKey(Member, on_delete=models.CASCADE)
    def __str__(self):
        return self.material
    
# class Rank(models.Model):
#     who = models.ForeignKey(Member, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.who.name