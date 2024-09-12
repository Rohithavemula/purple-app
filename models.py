from django.db import models
class Register(models.Model):
    Fullname=models.CharField(max_length=50)
    Email=models.CharField(primary_key=True,max_length=50)
    Password=models.CharField(max_length=15)
    address=models.CharField(max_length=100)
    Mobilenumber=models.CharField(max_length=15)
    desig=models.CharField(max_length=15,default="user")

    def __str__(self):
         return self.Email+" , "+self.Fullname
class contact(models.Model):
    Name=models.CharField(primary_key=True,max_length=30)
    Email=models.CharField(max_length=30)
    Subject=models.CharField(max_length=100)
    Message=models.CharField(max_length=400)
    def _str_(self):
        return self.Name
 
 
    
