from django.conf.urls import url
from appTwo import views

urlpatterns = [
    url(r'^$', views.help, name='help'),
    #url(r'^help/', views.help, name='help'),
    #url(r'^maria/', views.maria, name='maria'),
]
