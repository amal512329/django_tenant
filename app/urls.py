from django.urls import path
from app import views
from .views import CreateClientView

urlpatterns = [
    path('',views.index,name="index"),
    path('create-client',CreateClientView.as_view(),name="client"),
]