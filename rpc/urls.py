from django.conf.urls import url
# -*- coding: utf-8 -*-
from . import views
from django.core.urlresolvers import reverse
from django.utils.translation import activate
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, get_object_or_404, redirect

app_name = 'rpc'

urlpatterns = [
	url(r'^$', views.add, name='index'),
	url(r'^category=services/$', views.services, name='services'),
	url(r'^category=software/$', views.software, name='software'),
	url(r'^category=physical/$', views.physical, name='physical'),
	url(r'^all_products/$', views.products, name='products'),
	url(r'^description/identifiant=(?P<pk>[-\d.]+)&name=(?P<name>[-\w.(),+ ]+)&price=(?P<list_price>[-\d. ]+)&image=(?P<image>[-\w. \' \" \n  \s+_&=/  ]+)&descrip=(?P<description>[-\w. \' \" \n (),+ ]+)/$'
		, views.single, name='single'),

	url(r'^login/$', views.login_user, name='login'),
	url(r'^register/$', views.UserFormView.as_view(), name = 'register'),
	url(r'^logout/$', views.logout_user, name='logout'),

]




