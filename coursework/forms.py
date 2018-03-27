from django import forms
from .models import Continuous_Assessment

class Continuous_AssessmentForm(forms.ModelForm):
    class Meta:
        model=Continuous_Assessment
        fields=[
                'student_number',
                'subject_name',
                'Test_name',
                'Test_mark',
                ]
    def __init__(self,user=None,*args,**kwargs):
        print(user)
    
        #print(kwargs.pop('user'))
   
        #print(kwargs.pop('instance'))
        super(Continuous_AssessmentForm,self).__init__(*args,**kwargs)
        
        

