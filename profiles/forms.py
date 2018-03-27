from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model
from .models import Profile
User=get_user_model()



class RegisterForm(UserCreationForm):
    
    password1=forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Password confirmation',widget=forms.PasswordInput)
    
    class Meta(UserCreationForm.Meta):
        model=Profile
        fields=('username','email','is_student','is_teacher','is_admin','school','class_teacher')                          
    

    
    def clean_email(self):
        email=self.cleaned_data.get("email")
        qs=User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("Email Already in use")
        return email

    def clean_password2(self):
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("passwords do not match")
        return password2
    def save(self,commit=True):
        user=super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active=False
        if commit:
            user.save()
        return user
class UpdateForm(UserChangeForm):
    class Meta:
        model=Profile
        fields=UserChangeForm.Meta.fields
    def clean_email(self):
        email=self.cleaned_data.get("email")
        qs=User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("Email Already in use")
        return email

    def clean_password2(self):
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("passwords do not match")
        return password2
    def save(self,commit=True):
        user=super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active=False
        if commit:
            user.save()
        return user
