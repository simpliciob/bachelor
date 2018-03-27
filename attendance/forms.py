from django import forms
from .models import Attendance

class AttendanceForm(forms.ModelForm):

    
    class Meta:
        
        model=Attendance
        fields=[
            'student_number',
            'date',
            'status',
            'reason_of_absence',
            
             ]
        
    def __init__(self,user=None,*args,**kwargs):
        #print(kwargs.pop('user'))
        print(user)
        #print(kwargs.pop('instance'))
        super(AttendanceForm,self).__init__(*args,**kwargs)
         
    

        

