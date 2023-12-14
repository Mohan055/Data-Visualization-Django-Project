from datavisualization import views
from django.urls import path

app_name = 'datavisualization'

urlpatterns = [
    path('',views.index,name='dashboard'),

    
]