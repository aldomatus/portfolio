#   Django
from django.contrib import admin
from django.urls import path, include

#   Imported Urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Profile.urls'))
]
