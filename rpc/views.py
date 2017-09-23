# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.utils.translation import activate
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect 
import sys
import xmlrpclib
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import ugettext as _
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserForm
from django.views.generic import View


def add(request):
	url = 'http://localhost:8069'
	db = 'odoodjangoconnector'
	username = 'admin'
	password = 'admin'
	common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
	uid = common.authenticate(db, username, password, {})
	models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

	record = models.execute_kw(db, uid, password,
	'product.template', 'search_read',[[['create_uid', '=', 1]]], {'fields': ['id','test', 'description','image_medium', 'name','list_price']})
	
	category = models.execute_kw(db, uid, password,
		'product.template', 'search_read',[[['create_uid', '=', 1]]], {'fields': ['categ_id','name',]} )
	x = [x.get('id',) for x in record]
	print '____fff__', x
	if request.user.is_authenticated():
		base_template_name = 'base.html'
	else:
		base_template_name = 'basevisitor.html'


	return render(request, 'rpc/index.html',
		{'product':record,'category' : category ,'product_range' : record[:4],'base_template_name':base_template_name})



def services(request):
	url = 'http://localhost:8069'
	db = 'odoodjangoconnector'
	username = 'admin'
	password = 'admin'
	common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
	uid = common.authenticate(db, username, password, {})
	models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
	
	category = models.execute_kw(db, uid, password,
		'product.template', 'search_read',[[['categ_id', '=', 4]]], {'fields': ['id', 'description','image_medium', 'name','list_price',]} )

	#x = [x.get('name','image_medium') for x in record]
	#y = [y.get('name') for y in record]
	print '___IDS____', category
	page = request.GET.get('page', 1)

	paginator = Paginator(category, 8)
	try:
		cat = paginator.page(page)
	except PageNotAnInteger:
		cat = paginator.page(1)
	except EmptyPage:
		cat= paginator.page(paginator.num_pages)
	text = "Services"	
	
	return render(request, 'rpc/category.html',{'category': category,'cat':cat, 'text':text})


def software(request):
	url = 'http://localhost:8069'
	db = 'odoodjangoconnector'
	username = 'admin'
	password = 'admin'
	common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
	uid = common.authenticate(db, username, password, {})
	models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
	
	category = models.execute_kw(db, uid, password,
		'product.template', 'search_read',[[['categ_id', '=', 5]]], {'fields': ['id', 'description','image_medium', 'name','list_price',]} )

	
	#x = [x.get('name','image_medium') for x in record]
	#y = [y.get('name') for y in record]
	print '___IDS____', category

	page = request.GET.get('page', 1)

	paginator = Paginator(category, 8)
	try:
		cat = paginator.page(page)
	except PageNotAnInteger:
		cat = paginator.page(1)
	except EmptyPage:
		cat= paginator.page(paginator.num_pages)

	text = "Software"
	return render(request, 'rpc/category.html',{'category': category,'cat':cat,'text':text})

def physical(request):
	url = 'http://localhost:8069'
	db = 'odoodjangoconnector'
	username = 'admin'
	password = 'admin'
	common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
	uid = common.authenticate(db, username, password, {})
	models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
	
	category = models.execute_kw(db, uid, password,
		'product.template', 'search_read',[[['categ_id', '=', 6]]], {'fields': ['id', 'description','image_medium', 'name','list_price',]} )

	
	#x = [x.get('name','image_medium') for x in record]
	#y = [y.get('name') for y in record]
	print '___IDS____', category

	page = request.GET.get('page', 1)

	paginator = Paginator(category, 8)
	try:
		cat = paginator.page(page)
	except PageNotAnInteger:
		cat = paginator.page(1)
	except EmptyPage:
		cat= paginator.page(paginator.num_pages)

	text = "Physical"
	return render(request, 'rpc/category.html',{'category': category,'cat':cat,'text':text,})



def products(request):
	url = 'http://localhost:8069'
	db = 'odoodjangoconnector'
	username = 'admin'
	password = 'admin'
	common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
	uid = common.authenticate(db, username, password, {})
	models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
	
	category = models.execute_kw(db, uid, password,
		'product.template', 'search_read',[[['create_uid', '=', 1]]], {'fields': ['id','description', 'image_medium', 'name','list_price',]} )

	#x = [x.get('name','image_medium') for x in record]
	#y = [y.get('name') for y in record]
	x = [x.get('description',) for x in category]
	print '____fff__', x
	#print '___IDS____', category
	page = request.GET.get('page', 1)

	paginator = Paginator(category, 8)
	try:
		cat = paginator.page(page)
	except PageNotAnInteger:
		cat = paginator.page(1)
	except EmptyPage:
		cat= paginator.page(paginator.num_pages)
	text = _("All Products")	
	
	return render(request, 'rpc/category.html',{'category': category,'cat':cat, 'text':text})


def single(request, pk,name,list_price, image,description):

	url = 'http://localhost:8069'
	db = 'odoodjangoconnector'
	username = 'admin'
	password = 'admin'
	common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
	uid = common.authenticate(db, username, password, {})
	models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
	
	category = models.execute_kw(db, uid, password,
		'product.template', 'search_read',[[['create_uid', '=', 1]]], {'fields': ['id', 'description','image_medium', 'name','list_price',]} )

	translate = models.execute_kw(db, uid, password,
		'ir.translation', 'search_read',[[['name', '=',"product.template,description"]]], {'fields': ['id','res_id', 'value','src']} )
	#print 'description', description


	d = [d for d in translate if d["src"] == description]
	x = d[0]['value']



	

	
		# mydict = {'george':16,'amber':19}
		# print mydict.keys()[mydict.values().index(16)] 

	return render(request,'rpc/single-product.html',
	 {'category':category,'pk':pk,'name':name,'list_price':list_price,'descr':description,'trans':x, 'image':image})




class UserFormView(View):
	form_class = UserForm
	template_name = 'rpc/registration.html'



	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	#process from data
	
	def post(self, request):
		form = self.form_class(request.POST)
	
		if form.is_valid():

			user = form.save(commit=False)

			#cleaned data

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			# returns user objects if credentials are correct
			user = authenticate(username=username, password= password)
			messages.add_message(request, messages.SUCCESS, 'Your account were successfully created.')
			
			if user is not None:

				if user.is_active:
					login(request, user)
					base_template_name = 'base.html'
					model = Post
					return render(request, 'rpc/index.html',{'base_template_name':base_template_name}) 
		return render (request, self.template_name, {'form': form})


def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				base_template_name = 'base.html'
				return render(request, 'rpc/index.html', {'base_template_name':base_template_name})
			else:
				return render(request, 'rpc/login.html', {'error_message': 'Your account has been disabled'})
		else:
			return render(request, 'rpc/login.html', {'error_message': 'Invalid login'})
	return render(request, 'rpc/login.html')