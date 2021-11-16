from . import views
from django.urls import path


app_name = "webInterface"

urlpatterns = [
    path('',views.home,name = 'home'),
]