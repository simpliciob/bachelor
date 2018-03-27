from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ExamMarkForm
from .models import ExamMark
from django.urls import reverse
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

class ExamMarkListView(ListView,LoginRequiredMixin):
    def get_queryset(self):
        return ExamMark.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(ExamMarkListView, self).get_context_data(*args,**kwargs)
        query=self.request.GET.get('q')
        qs=ExamMark.objects.filter(user=self.request.user).search(query)
    
        
            
        if qs.exists():
            context['locations']=qs
        
        return context
 
    
class ExamMarkDetailView(DetailView,LoginRequiredMixin):
    def get_queryset(self):
        return ExamMark.objects.filter(user=self.request.user)
    
    
class ExamMarkCreateView(LoginRequiredMixin,CreateView):
    form_class=ExamMarkForm
    login_url='/login/'
    template_name="exams/forms.html"
    success_url='/create/'
    def get_queryset(self):
        return ExamMark.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(ExamMarkCreateView,self).get_context_data(*args,**kwargs)
        context['title']='Add Exam Marks'
        return context
    def form_valid(self, form):
        obj=form.save(commit=False)
        obj.user=self.request.user
        return super(ExamMarkCreateView,self).form_valid(form)
    def get_form_kwargs(self):
        kwargs=super(ExamMarkCreateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs
    def get_success_url(self):
        return reverse('exams:addmark')

    
    
class ExamMarkUpdateView(LoginRequiredMixin,UpdateView):
    template_name="exams/detail-update.html"
    form_class=ExamMarkForm
    def get_queryset(self):
        return ExamMark.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(ExamMarkUpdateView,self).get_context_data(*args,**kwargs)
        context['title']='Update Exam Marks'
        return context
    def get_form_kwargs(self):
        kwargs=super(ExamMarkUpdateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs
    def get_success_url(self):
        return reverse('exams:examlist')
   

class ReportCreateView(LoginRequiredMixin,CreateView):
    form_class=ExamMarkForm
    login_url='/login/'
    template_name="exams/forms.html"
    success_url='/create/'
    def get_queryset(self):
        return ExamMark.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(ExamMarkCreateView,self).get_context_data(*args,**kwargs)
        context['title']='Add Exam Marks'
        return context
    def form_valid(self, form):
        obj=form.save(commit=False)
        obj.user=self.request.user
        return super(ExamMarkCreateView,self).form_valid(form)
    def get_form_kwargs(self):
        kwargs=super(ExamMarkCreateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs

class ExamMarkDeleteView(LoginRequiredMixin,DeleteView):
    model=ExamMark
    template_name="exams/delete_mark.html"
    form_class=ExamMarkForm
    def get_context_data(self,*args,**kwargs):
        context_data=super(ExamMarkDeleteView,self).get_context_data(*args,**kwargs)
        pk=self.kwargs.get('pk')
        examMark=ExamMark.objects.get(id=int(pk))
        context_data.update({'examMark':examMark})
        return context_data
    def get_success_url(self):
        return reverse('exams:examlist')
   






# Create your views here.


# Create your views here.
