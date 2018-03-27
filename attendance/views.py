from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AttendanceForm
from .models import Attendance
from django.views.generic import ListView,DetailView,CreateView,UpdateView,View

class HomeView(View):
    def get(self,request,*args,**kwargs):
        if not request.user.is_authenticated():
            return render(request, "home.html",{})
        user=request.user
        
        is_following_user_ids=[x.user.id for x in user.is_following.all()]
        qs=Attendance.objects.filter(user__id__in=is_following_user_ids).order_by("student_number")[:5]
        for x in user.is_following.all():
            return render(request, "attendance/home-feed.html",{"object_list":qs})

class AttendanceListView(ListView):
    def get_queryset(self):
        return Attendance.objects.filter(user=self.request.user)
    
class AttendanceDetailView(DetailView):
    def get_queryset(self):
        return Attendance.objects.filter(user=self.request.user)

class AttendanceCreateView(LoginRequiredMixin,CreateView):
    form_class=AttendanceForm
    login_url='/login/'
    template_name="attendance/forms.html"
    success_url="/"
    def get_queryset(self):
        return Attendance.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(AttendanceCreateView,self).get_context_data(*args,**kwargs)
        context['title']='Add Attendance'
        return context
    def form_valid(self, form):
        obj=form.save(commit=False)
        obj.user=self.request.user
        return super(AttendanceCreateView,self).form_valid(form)
    def get_form_kwargs(self):
        kwargs=super(AttendanceCreateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs

class AttendanceUpdateView(LoginRequiredMixin,UpdateView):
    template_name="attendance/detail-update.html"
    form_class=AttendanceForm
    def get_queryset(self):
        return Attendance.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(AttendanceUpdateView,self).get_context_data(*args,**kwargs)
        context['title']='Update Attendance'
        return context
    def get_form_kwargs(self):
        kwargs=super(AttendanceUpdateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs




# Create your views here.


# Create your views here.


# Create your views here.
