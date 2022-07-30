from django.urls import path
from mainApp import views

urlpatterns = [
    path('',views.IndexPage),
    path('delete/<int:id>/', views.delete_data,name='deletedata'),
    path('updatedata/<int:id>/', views.update_data,name='updatedata')
]
