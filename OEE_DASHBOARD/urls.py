# OEE_DASHBOARD\\urls.py

from django.urls import path
from .views import HomePageView, AboutPageView, DA5PageView, DA6PageView, BB1PageView, BB2PageView, GE3PageView, DA7PageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('da5/', DA5PageView.as_view(), name = 'DA5' ),
    path('da6/', DA6PageView.as_view(), name = 'DA6' ),
    path('bb1/', BB1PageView.as_view(), name = 'BB1' ),
    path('bb2/', BB2PageView.as_view(), name = 'BB2' ),
    path('ge3/', GE3PageView.as_view(), name = 'GE3' ),
    path('da7/', DA7PageView.as_view(), name = 'DA7' )
]
