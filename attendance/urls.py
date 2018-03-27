
from django.conf.urls import url,include
from .views import (AttendanceListView,
                    AttendanceCreateView,
                    AttendanceDetailView,
                    AttendanceUpdateView,
                   
                    )
    

urlpatterns = [
    
    url(r'^(?P<pk>\d+)/$',AttendanceDetailView.as_view(),name="attendance-detail"),
    url(r'^$', AttendanceListView.as_view(),name="attendancelist"),
    url(r'^create/$',AttendanceCreateView.as_view(),name="addattendance"),
    url(r'^(?P<pk>[\w-]+)/update/$',AttendanceUpdateView.as_view(),name="updateattendance"),
    
    
    
]
