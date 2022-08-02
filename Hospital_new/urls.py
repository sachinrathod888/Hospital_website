"""Hospital_new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospital_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home, name='home'),
    path("signin/",views.login, name='login'),
    path("signup/",views.signup, name='signup'),
    path("logout/",views.logout, name='logout'),
    path("addpatient/",views.AddPatient, name='addpatient'),
    path("patientrecord/",views.PatientRecord, name='patientrecord'),
    path('<int:id>/',views.update_data,name="update"),
    path("delete/<int:id>/",views.delete_data,name='delete'),
    path('view/<int:id>/',views.view,name='view'),
    path('render_pdf/<int:id>/',views.render_pdf_view, name='render_pdf'),
    path('newinvoice',views.newinvoice,name='newinvoice'),
    
    
]
