
from django.conf.urls import url,include
from .views import (
                    Continuous_AssessmentListView,
                    AttendanceListView,
                    ExamMarkListView,
                    ReportsListView,
                    
                
                    
                    
                    
                    )
    

urlpatterns = [
    
        
    url(r'^$', Continuous_AssessmentListView.as_view(),name="studentscontinuous"),
    url(r'^attendance/$', AttendanceListView.as_view(),name="attendance"),
    url(r'^exammark/$', ExamMarkListView.as_view(),name="exammark"),
    url(r'^report/$', ReportsListView.as_view(),name="reportst"),
       
    
]
