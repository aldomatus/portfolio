#   Django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#   Imported Urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Profile.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
