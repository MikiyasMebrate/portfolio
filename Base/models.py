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
    img1 = models.ImageField(upload_to="project/", height_field=None, width_field=None, max_length=None)
    img2 = models.ImageField(upload_to="project/", height_field=None, width_field=None, max_length=None)
    img3 = models.ImageField(upload_to="project/", height_field=None, width_field=None, max_length=None)
    img4 = models.ImageField(upload_to="project/", height_field=None, width_field=None, max_length=None)
    project_type =models.CharField(max_length=50, null=True, blank=True)
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


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject =models.CharField(max_length=2000)
    message = models.TextField()


    def __str__(self) -> str:
        return self.name + " " + str(self.subject)