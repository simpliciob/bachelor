from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import DetailView,View,CreateView,UpdateView,ListView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.contrib.auth import get_user_model
from exams.models  import ExamMark
from .models import Profile
from django.urls import reverse
from .forms import RegisterForm,UpdateForm
User=get_user_model()
def activate_user_view(request, code=None,*args,**kwargs):
    if code:
        qs=Profile.objects.filter(activation_key=code)
        if qs.exists() and qs.count()==1:
            profile=qs.first()
            if not profile.activated:
                user_=profile.user
                user_.is_active=True
                user_.save()
                profile.activated=True
                profile.activation_key=None
                profile.save()
                return redirect("/login/")
    return redirect("/login/")
class ProfileListView(ListView,LoginRequiredMixin):
    def get_queryset(self):
        return Profile.objects.filter(class_teacher=self.request.user).filter(is_student=True)
class StudentListView(ListView,LoginRequiredMixin):
    template_name='/profiles/student_list.html'
    def get_queryset(self):
        return Profile.objects.filter(school=self.request.user).filter(is_student=True)
class TeacherListView(ListView,LoginRequiredMixin):
    tempelate_name='/profiles/teachers_list.html'
    def get_queryset(self):
        return Profile.objects.filter(school=self.request.user).filter(is_teacher=True)
    


class RegisterView(CreateView,LoginRequiredMixin):
    form_class=RegisterForm
    template_name="registration/register.html"
    success_url="/register/"
    def form_valid(self, form):
        obj=form.save(commit=False)
        obj.user=self.request.user
        return super(RegisterView,self).form_valid(form)
   
    
    #def dispatch(self,*args,**kwargs):
        #return redirect("/login/")
        #return super(RegisterView, self).dispatch(*args,**kwargs)
    
class ProfileFollowToggle(LoginRequiredMixin,View):
    def post(self,request,*args,**kwargs):
        
        username_to_toggle=request.POST.get("username")
        profile_, is_following=Profile.objects.toggle_follow(request.user,username_to_toggle)
        print(is_following)
       
            
        
        return redirect(f"/u/{profile_.user.username}/")

class ProfileDetailView(DetailView,LoginRequiredMixin):
    template_name="profiles/user.html"
    def get_object(self):
        username=self.kwargs.get("username")
        if username is None:
            raise Http404
        return get_object_or_404(User,username__iexact=username, is_active=True)
    
    def get_context_data(self,*args,**kwargs):
        context=super(ProfileDetailView, self).get_context_data(*args,**kwargs)
        user=context['user']
        is_following=False
        if user.profile in self.request.user.is_following.all():
            is_following=True
        context['is_following']=is_following
        query=self.request.GET.get("q")
        items_exists=ExamMark.objects.filter(user=user).exists()
        qs=ExamMark.objects.filter(user=user).search(query)
    
        
            
        if items_exists and qs.exists():
            context['locations']=qs
        
        return context
   
class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    template_name="profiles/detail-update.html"
    form_class=UpdateForm
    model=Profile
   
class ProfileDeleteView(LoginRequiredMixin,DeleteView):
    model=Profile
    template_name="profiles/delete_user.html"
    form_class=RegisterForm
    def get_context_data(self,*args,**kwargs):
        context_data=super(ProfileDeleteView,self).get_context_data(*args,**kwargs)
        pk=self.kwargs.get('pk')
        profile=Profile.objects.get(id=int(pk))
        context_data.update({'profile':profile})
        return context_data
    def get_success_url(self):
        return reverse('profiles:profilelist')
   



# Create your views here.
