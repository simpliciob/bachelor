from django.db import models
from django.db import models
from django.conf import settings
from .utils import code_generator
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractUser
User=settings.AUTH_USER_MODEL
class Profile(AbstractUser):
    is_student=models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)
    is_classTeacher=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    school=models.CharField(max_length=50)
    class_teacher=models.CharField(max_length=50,blank=True)
    REQUIRED_FIELDS=['email']
    def __str__(self):
        return self.username
    def get_absolute_url(self):
        return reverse('exams:update', kwargs={'pk':self.pk})


        


            
    
   


# Create your models here.
