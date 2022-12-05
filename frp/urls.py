from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('frpflexural', views.frpflexural, name='frpflexural'),
    path('frpflexuralA', views.frpflexuralA, name='frpflexuralA'),
    path('frpflexuralB', views.frpflexuralB, name='frpflexuralB'),
    path('frpshear', views.frpShearCalc, name='frpshear'),
    path('frpShearWall', views.frpShearWall, name='frpShearWall'),
    path('frpColumn', views.frpColumnCalc, name='frpColumn'),
    path('frpMonitor', views.frpMonitor, name='frpMonitor'),
    path('frpInstall', views.frpInstall, name='frpInstall'),
]

urlpatterns += staticfiles_urlpatterns()