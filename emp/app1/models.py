from django.db import models

# Create your models here.
class employee(models.Model):
    EMPLOYEE_ID=models.IntegerField()
    EMPLOYEE_NAME=models.CharField(max_length=20)
    SALARY=models.IntegerField()
    PLACE=models.CharField(max_length=20)
    img = models.FileField()
    def __str__ (self):
        return self.EMPLOYEE_NAME
