from django.db import models
from django.db import models
from datetime import date
from django.conf import settings
from django.db.models import Q
from django.core.urlresolvers import reverse
User=settings.AUTH_USER_MODEL
class Attendance(models.Model):
    
    user=models.ForeignKey(User)
    student_number=models.CharField(max_length=50,blank=False,null=False)
    date=models.DateField(default=date.today)
    STATUS=(
             ('A', 'Absent'),
             ('P',  'Present'),
            )
    status=models.CharField(max_length=1,choices=STATUS)
    reason_of_absence=models.TextField(blank=True)

    


    def get_absolute_url(self):
        return reverse('attendance:detail', kwargs={'pk':self.pk})
    def get_absolute_url(self):
        return reverse('attendance:updateattendance', kwargs={'pk':self.pk})
class AttendanceQuerySet(models.query.QuerySet):
    def search(self,query):
        if query:
            query=query.strip()
            return self.filter(Q(student_number__icontains=query)
                               ).distinct()
        return self
class AttendanceManager(models.Manager):
    def get_queryset(self):
        return AttendanceQuerySet(self.model,using=self._db)
        
    def search(self,query):
        return self.get_queryset().search(query)
    

# Create your models here.

# Create your models here.
