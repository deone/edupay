from django.conf.urls import url
from django.contrib import admin

from savings import views

urlpatterns = [
    url(r'^school/new', views.SchoolCreate.as_view()),
    url(r'^admin/', admin.site.urls),
]
