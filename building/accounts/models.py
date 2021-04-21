from django.db import models

# Create your models here.
class Building(models.Model):
	name = models.CharField(max_length=200, null=True)
	location = models.CharField(max_length=200, null=True)
	owner = models.CharField(max_length=200, null=True)
	unitscount = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.name

class Tenant(models.Model):
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	Phone = models.CharField(max_length=200, null=True)
	nextofkin = models.CharField(max_length=200, null=True)
	def __str__(self):
		return self.name

class BuildingTenant(models.Model):
	STATUS = (
			('Active', 'Active'),
			('Inactive', 'Inactive'),
			)

	building = models.ForeignKey(Building, null=True, on_delete= models.SET_NULL)
	tenant = models.ForeignKey(Tenant, null=True, on_delete= models.SET_NULL)
	chekindate = models.DateTimeField(auto_now_add=True, null=True)
	contractAmount=models.IntegerField()
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	def __str__(self):
		return self.status
	




class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name






	
