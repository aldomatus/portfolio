#   Django
from django.contrib import admin
from django.urls import path, include


#   urls 
from todos import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todos.urls'))
]
