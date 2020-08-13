from django.urls import path
from django.contrib import admin
from django.urls import path, include
from .views import UserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', UserView.as_view())
]
