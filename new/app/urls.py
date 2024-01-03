from django.conf.urls import url
from . import views
app_name='arka'

urlpatterns=[
    url(r'^$', views.base, name='base'),
    url(r'^aboutUs$', views.about, name='about'),
    url(r'^contact$', views.contactUs, name='contact'),

]
