from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    
    path('buildings/', views.listbuilding, name="buildings"),
    path('tenants/', views.listtenant, name="tenants"),
    path('listtenantbuilding/', views.listtenantbuilding, name="listtenantbuilding"),
    path('create/', views.createbuilding, name="create"),
    path('addtenant/', views.createtenant, name="addtenant"),
    path('createtenantbuilding/', views.createtenantbuilding, name="createtenantbuilding"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('deletetenant/<int:id>', views.deletetenant, name="deletetenant"),
    path('deletetenantbuilding/<int:id>', views.deletetenantbuilding, name="deletetenantbuilding"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('edit/update/<int:id>', views.update, name="update"),

    path('', views.home, name="home"),
    

]