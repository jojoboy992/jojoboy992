from django.urls import path
from .views import (
    homePageView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)
from .views import loginView
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from .views import *
from django.conf import os

from django.conf.urls.static import static

urlpatterns = [
    path("image_upload/", avatarView, name="image_upload"),
    path("success/", uploadok, name="success"),
    path("", homePageView.as_view(), name="home"),
    path("login/", loginView, name="login"),
    path("<int:pk>", BlogDetailView.as_view(), name="content_prev"),
    path("post/new", BlogCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/edit", BlogUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete", BlogDeleteView.as_view(), name="post_delete"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns = [path("", homePageView.as_view(), name="home"), path("login", loginView)]
