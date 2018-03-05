from django.conf.urls import url
from django.contrib import admin

from savings import views

urlpatterns = [
    url(r'^school/new', views.create_school),
    url(r'^agent/new', views.AgentCreate.as_view()),
    # url(r'^parent/new', views.create_parent),
    url(r'^admin/', admin.site.urls),
]
