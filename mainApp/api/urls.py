from django.urls import path,include
from mainApp.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('EmployeeAPI',views.EmployeeModelViewset,basename='Employee')

urlpatterns = [
    path('',include(router.urls)),
]
   
