from django.db import models

# Create your models here.
class Education(models.Model):
    school = models.CharField(max_length=100)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    degree = models.CharField(max_length=50)
    study = models.CharField(max_length=50)

    def __str__(self):
        return self.degree
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title
    
class History(models.Model):
    title = models.CharField(max_length=50)
    institution = models.CharField(max_length=100)
    role = models.TextField()
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.institution
