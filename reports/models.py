from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models import Q
User=settings.AUTH_USER_MODEL


class ReportsQuerySet(models.query.QuerySet):
    def search(self,query):
        if query:
            query=query.strip()
            return self.filter(Q(student_number__icontains=query)
                               ).distinct()
        return self
class ReportsManager(models.Manager):
    def get_queryset(self):
        return ReportsQuerySet(self.model,using=self._db)
        
    def search(self,query):
        return self.get_queryset().search(query)
    
    
class Reports(models.Model):
    user=models.ForeignKey(User)
    student_number=models.CharField(max_length=200)
    comments= models.TextField(max_length=200,blank=False,null=False)
    behaviour=models.CharField(max_length=50)
    class_position=models.IntegerField()
    achievements=models.CharField(max_length=50)
    comments=models.TextField(max_length=200)
    announcement=models.TextField(max_length=200)
    objects=ReportsManager()
    def __str__(self):
        return self.student_number


    def get_absolute_url(self):
        return reverse('reports:detail', kwargs={'pk':self.pk})
    #def get_absolute_url(self):
        return reverse('reports:update', kwargs={'pk':self.pk})
    #def get_absolute_url(self):
        return reverse('reports:delete', kwargs={'pk':self.pk})


    
# Create your models here.


# Create your models here.


# Create your models here.
