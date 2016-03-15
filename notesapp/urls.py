"""notesapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from notes.views import *
from notes.signals import *

urlpatterns = [
    #url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^$', custom_login),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/login/$', custom_login),
    url(r'^logout/$', logout_page),
    # url(r'^register/$', register),
    url(r'^register/$', UserView.as_view()),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
    url(r'^notes/$', NotesView.as_view(), name='new_notes'),
    url(r'^all_notes/$', NotesList.as_view()),
    url(r'^something1/(?P<some_num>.*)/something2/(?P<some_num_2>.*)/something_3/new/$', SomeView.as_view())
    #url(r'^admin/', admin.site.urls),
]
