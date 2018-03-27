
from django.conf.urls import url,include
from .views import (ReportsListView,
                    ReportsCreateView,
                    ReportsDeleteView,
                    ReportsUpdateView,
                    ReportsDetailView,
                    
                    )
    

urlpatterns = [
    
    url(r'^(?P<pk>\d+)/$',ReportsDetailView.as_view(),name="detail"),
    url(r'^list/$', ReportsListView.as_view(),name="reportlist"),
    url(r'^create/$',ReportsCreateView.as_view(),name="addreport"),
    url(r'^(?P<pk>[\w-]+)/delete/$',ReportsDeleteView.as_view(),name="delete",),
    url(r'^(?P<pk>[\w-]+)/update/$',ReportsUpdateView.as_view(),name="update",)
    
    
    
    
]
