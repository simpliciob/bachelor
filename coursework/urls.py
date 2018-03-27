
from django.conf.urls import url,include
from .views import (
                    Continuous_AssessmentListView,
                    Continuous_AssessmentDetailView,
                    Continuous_AssessmentCreateView,
                    Continuous_AssessmentUpdateView,
                    Continuous_AssessmentDeleteView
                    )
    

urlpatterns = [
    
        
    
    url(r'^(?P<pk>[\w-]+)/update$',Continuous_AssessmentUpdateView.as_view(),name="update"),
    url(r'^(?P<pk>[\w-]+)/delete$',Continuous_AssessmentDeleteView.as_view(),name="delete"),
    url(r'^$', Continuous_AssessmentListView.as_view(),name="listcontinuous"),
    url(r'^create/$',Continuous_AssessmentCreateView.as_view(),name="addcontinuous"),
    url(r'^(?P<pk>[\w-]+)/$',Continuous_AssessmentDetailView.as_view(),name="detail")
    
    
]
