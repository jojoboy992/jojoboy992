from django.contrib import admin
from django.urls import path, include
from pages.views import loginView
from django.conf import settings

from django.conf.urls.static import static

from pages.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pages/", include("pages.url")),
    path("login/", loginView, name="login"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.url")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
