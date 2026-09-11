from django.contrib import admin
from django.urls import include, path, re_path

from .views import frontend, frontend_asset


urlpatterns = [
    path("admin/", admin.site.urls),

    # Django REST API
    path("api/", include("games.urls")),

    # React assets
    re_path(
        r"^assets/(?P<path>.*)$",
        frontend_asset,
        name="frontend-asset",
    ),

    # React frontend / React Router
    re_path(
        r"^(?!api/|admin/|assets/).*$",
        frontend,
        name="frontend",
    ),
]