from django.urls import path
from . import views
urlpatterns = [
      path('', views.home, name='home'),
      path('contact.html', views.contact, name='contact'),
      path('about.html', views.about, name='about'),
      path('service.html', views.service, name='service'),
      path('team.html', views.team, name='team'),
      path('portfolio.html', views.portfolio, name='portfolio'),




]
