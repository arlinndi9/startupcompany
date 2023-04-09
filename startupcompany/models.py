from django.db import models

class Team(models.Model):
    name=models.CharField(max_length=255 )
    lastname=models.CharField(max_length=255)
    pozita=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return "{} - {} - {} - {}".format(self.name,self.lastname ,self.pozita,self.email)
# Create your models here9.
class Stories(models.Model):
    title_stories=models.CharField(max_length=255)
    content_stories=models.TextField()
    date_stories=models.DateTimeField()
    def __str__(self):
         return self.title_stories
class Jobs(models.Model):
    position_name=models.CharField(max_length=255)
    position_requirement=models.TextField()
    def __str__(self):
        return self.position_name

class Contact(models.Model):
    name=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)
    content=models.TextField(null=False,default='')
    def __str__(self):
        return self.name

class apply_job(models.Model):
    CHOICES = (('Backend Developer', 'Backend Developer'), ('Fullstack Developer', 'Fullstack Developer'),
               ('Frontend Developer', 'Frontend Developer'),
               ('Fullstack Developer internship', 'Fullstack Developer internship'),)
    name=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    email=models.EmailField()
    positionjob= models.CharField(max_length=255,choices=CHOICES)
    about=models.TextField()
    resume=models.FileField(null=True,blank=True,upload_to='resumes/')
    coverletter=models.FileField(null=True,blank=True,upload_to='resumes/')
    def __str__(self):
        return self.name


