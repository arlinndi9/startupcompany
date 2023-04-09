
from django.urls import path,include
from . import views
from startupcompany.models import Stories
urlpatterns = [
    path('home/',views.home,name='home'),
    path('stories/',views.stories,name='stories'),
    path('about/',views.about,name='about'),
    path('career/',views.career,name='career'),
    path('career/apply',views.career_apply,name='apply'),
    path('contact/',views.contact,name='contact'),


]
