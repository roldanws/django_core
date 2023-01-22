from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import urls
from core.urls import core_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(urls)),
    path('', include(core_patterns)),
]
