from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from savings import views
from accounts import views as accounts_views
from cashbook import views as cashbook_views

from accounts.forms import LoginForm

urlpatterns = [
    url(r'^$', auth_views.login, {
        'template_name': 'accounts/login.html',
        'authentication_form': LoginForm
    }, name='login'),
    url(r'^logout$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^request_parent$', views.request_parent),
    url(r'^record_payment$', views.record_payment),

    url(r'^dashboard/savings', views.savings, name='savings'),
    url(r'^dashboard', views.dashboard, name='dashboard'),

    url(r'^cashbook', cashbook_views.index, name='cashbook'),
    url(r'^school/new', views.create_school, name='new_school'),
    url(r'^agent/new', views.create_agent, name='new_agent'),
    url(r'^parent/new', views.create_parent, name='new_parent'),
    url(r'^admin/', admin.site.urls),
]
