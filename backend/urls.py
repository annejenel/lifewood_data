from django.urls import path, include

urlpatterns = [
    path("api/", include("applications.urls")),  # This ensures `api/contact/` works
]
