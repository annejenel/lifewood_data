from django.urls import path
from applications.views import ApplicationCreateView, ContactMessageCreateView

urlpatterns = [
    path("applications/", ApplicationCreateView.as_view(), name="application-create"),
    path("contact/", ContactMessageCreateView.as_view(), name="contact-message"),
]
