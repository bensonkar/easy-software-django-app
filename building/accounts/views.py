from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.
from .models import *
from .forms import CreateUserForm

# registration
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)
# login page
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)
#logout page
def logoutUser(request):
	logout(request)
	return redirect('login')

#dashboard
@login_required(login_url='login')
def home(request):
	
	buildings = Building.objects.all()
	buildings =Building.objects.all()
	bcount =buildings.count()
	tenants =Tenant.objects.all()
	tcount =tenants.count()
	

	#total_orders = orders.count()
	#delivered = orders.filter(status='Delivered').count()
	#pending = orders.filter(status='Pending').count()

	context = {'buildings':buildings,'bcount':bcount,'tcount':tcount }

	return render(request, 'accounts/dashboard.html', context)
#creating building
@login_required(login_url='login')
def createbuilding(request):
	if request.method == 'POST':
		building = Building(
		name=request.POST.get('name'), 
		location=request.POST.get('location'),
		owner=request.POST.get('owner'),
		unitscount=request.POST.get('unitcount')
		)
		building.save()
		messages.success(request, 'Building was created ')
		return redirect('buildings')
			

		
	return render(request, 'accounts/createbuilding.html')

#creating tenant
@login_required(login_url='login')
def createtenant(request):
	if request.method == 'POST':
		tenant = Tenant(
		name=request.POST.get('name'), 
		email=request.POST.get('email'),
		Phone=request.POST.get('phone'),
		nextofkin=request.POST.get('nextofkin')
		)
		tenant.save()
		messages.success(request, 'Tenant was created ')
		return redirect('tenants')
	return render(request, 'accounts/createtenant.html')
			

#creating tenantbuilding
@login_required(login_url='login')
def createtenantbuilding(request):
	if request.method == 'POST':
		
		buildingtenant = BuildingTenant(
		building=request.POST.get('building'), 
		tenant=request.POST.get('tenant'),
		chekindate=datetime.datetime.now(),
		contractAmount=request.POST.get('contractAmount'),
		status=request.POST.get('status')
		)
		buildingtenant.save()
		messages.success(request, 'Tenant was created ')
		return redirect('buildingtenants')
			


	buildings =Building.objects.all()
	
	tenants =Tenant.objects.all()

	context = {'buildings':buildings, 'tenants':tenants }	
	return render(request, 'accounts/createbuildingtenant.html',context)
#delete building	
@login_required(login_url='login')
def delete(request, id):
    building = Building.objects.get(id=id)
    building.delete()
    return redirect('buildings') 

#delete tenant	
@login_required(login_url='login')
def deletetenant(request, id):
    tenant = Tenant.objects.get(id=id)
    tenant.delete()
    return redirect('tenants') 
#delete tenant building	
@login_required(login_url='login')
def deletetenantbuilding(request, id):
    tenantbuilding = BuildingTenant.objects.get(id=id)
    tenantbuilding.delete()
    return redirect('listtenantbuilding') 

@login_required(login_url='login')
def edit(request, id):
    buildings = Building.objects.get(id=id)
    context = {'buildings': buildings}
    return render(request, 'accounts/editbuilding.html', context)

@login_required(login_url='login')
def update(request, id):
	building = Building.objects.get(id=id)
	building.name = request.POST.get('name')
	building.location = request.POST.get('location')
	building.owner = request.POST.get('owner')
	building.unitscount = request.POST.get('unitscount')
	building.save()
	return redirect('buildings')


@login_required(login_url='login')
def listbuilding(request):
	if request.method =='GET':
		buildings = Building.objects.all()
		context = {'buildings': buildings}
		return render(request, 'accounts/building.html', context)

#tenant listing
@login_required(login_url='login')
def listtenant(request):
	if request.method =='GET':
		tenants = Tenant.objects.all()
		context = {'tenants': tenants}
		return render(request, 'accounts/tenant.html', context)
#tenant building listing		
@login_required(login_url='login')
def listtenantbuilding(request):
	if request.method =='GET':
		tenantbuildings = BuildingTenant.objects.all()
		context = {'tenantbuildings': tenantbuildings}
		return render(request, 'accounts/tenantbuilding.html', context)






