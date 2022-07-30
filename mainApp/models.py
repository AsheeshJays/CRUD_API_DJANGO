from django.db import models

class Employee(models.Model):
    eid = models.AutoField(primary_key=True)
    empID = models.CharField(max_length=50)
    empName = models.CharField(max_length=50)
    empDesgination = models.CharField(max_length=50)
    empSalary = models.CharField(max_length=50)

    def __str__(self):
        return self.empName
    