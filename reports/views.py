from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ReportsForm
from .models import Reports
from django.urls import reverse
from exams .models import ExamMark
from profiles .models import Profile
from django.views.generic import ListView,DetailView,CreateView,UpdateView,View,DeleteView

class HomeView(View):
    def get(self,request,*args,**kwargs):
        #if not request.user.is_authenticated():
        return render(request, "exams/home.html",{})
        #user=request.user
        
        #is_following_user_ids=[x.user.id for x in user.is_following.all()]
        #qs=ExamMark.objects.filter(user__id__in=is_following_user_ids).order_by("student_number")[:5]
        #for x in user.is_following.all():
            #return render(request, "teachers/home-feed.html",{"object_list":qs})

class ReportsListView(ListView,LoginRequiredMixin):
    template_name="reports/reports_list.html"
    context_object_name = 'reports_list'
    def get_queryset(self):
        user=self.request.user
        return Reports.objects.filter(user=self.request.user)
        
        
    
class ReportsDetailView(DetailView):
    def get_queryset(self):
        return ExamMark.objects.all()
     
    
    
class ReportsCreateView(LoginRequiredMixin,CreateView):
    form_class=ReportsForm
    login_url='/login/'
    template_name="reports/forms.html"
    def get_queryset(self):
        return Reports.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(ReportsCreateView,self).get_context_data(*args,**kwargs)
        context['title']='Add Report'
        return context
    def form_valid(self, form):
        obj=form.save(commit=False)
        obj.user=self.request.user
        return super(ReportsCreateView,self).form_valid(form)
    def get_form_kwargs(self):
        kwargs=super(ReportsCreateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs
    def get_success_url(self):
        return reverse('reports:addreport') 

    
class ReportsUpdateView(LoginRequiredMixin,UpdateView):
    template_name="reports/detail-update.html"
    form_class=ReportsForm
    def get_queryset(self):
        return Reports.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(ReportsUpdateView,self).get_context_data(*args,**kwargs)
        context['title']='Update Exam Marks'
        return context
    def get_form_kwargs(self):
        kwargs=super(ReportsUpdateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs
    def get_success_url(self):
        return reverse('reports:reportlist')

   
class ReportsDeleteView(LoginRequiredMixin,DeleteView):
    model=Reports
    template_name="reports/delete_report.html"
    form_class=ReportsForm
    def get_context_data(self,*args,**kwargs):
        context_data=super(ReportsDeleteView,self).get_context_data(*args,**kwargs)
        pk=self.kwargs.get('pk')
        reports=Profile.objects.get(id=int(pk))
        context_data.update({'reports':reports})
        return context_data
    def get_success_url(self):
        return reverse('reports:reportlist')
   




# Create your views here.


# Create your views here.


# Create your views here.
