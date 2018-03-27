from django import forms
from .models import Reports

class ReportsForm(forms.ModelForm):
    
    
    class Meta:
        
        model=Reports
        fields=[
            'student_number',
            'class_position',
            'comments',
            'behaviour',
            'achievements',
            'announcement',
             ]
    def __init__(self,user=None,*args,**kwargs):
        #print(kwargs.pop('user'))
        print(user)
        #print(kwargs.pop('instance'))
        super(ReportsForm,self).__init__(*args,**kwargs)
         
    

                

