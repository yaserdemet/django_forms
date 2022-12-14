from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    ##* upload_to nereye kaydedileceğini belirler.

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
    ##? __str__ görüntü amaclı olusturulur.