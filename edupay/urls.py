from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from savings import views
from accounts import views as accounts_views

from accounts.forms import LoginForm

urlpatterns = [
    url(r'^$', auth_views.login, {
        'template_name': 'accounts/login.html',
        'authentication_form': LoginForm
    }, name='login'),
    url(r'^logout$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^dashboard', accounts_views.dashboard),
    url(r'^school/new', views.create_school),
    url(r'^agent/new', views.AgentCreate.as_view()),
    # url(r'^parent/new', views.create_parent),
    url(r'^admin/', admin.site.urls),
]
