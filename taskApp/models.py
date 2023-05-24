from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email= models.EmailField()   
    phone_number = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    # PHONE_NUMBER_FIELD = 'phone_number'
    # USERNAME_FIELD = 'phone_number'
    # REQUIRED_FIELDS = []

    def __str__(self) :
        return self.first_name
# class User(AbstractUser):
    # PHONE_NUMBER_FIELD = 'phone_number'
    # username = None
    # email = None
    # phone_number = models.CharField(max_length=20, unique=True)

    # USERNAME_FIELD = 'phone_number'
    # REQUIRED_FIELDS = []

    # def __str__(self):
    #     return self.phone_number

class Task(models.Model):
    STATUS_CHOICES = (
        ('started', 'Started'),
        ('pending','Pending'),
        ('finished', 'Finished'),
        ('blocked', 'Blocked'),
    )
    task_name = models.CharField(max_length=30)
    descriptions =models.CharField(max_length=150)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='started')   
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    
    def __str__(self):
        return self.task_name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tasks = models.ManyToManyField(Task, blank=True, related_name='employees')

    def __str__(self):
        return self.user.phone_number        