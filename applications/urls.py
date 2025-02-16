from django.urls import path
from applications.views import ApplicationCreateView, ContactMessageCreateView, AdminLoginView, ApplicationListView

urlpatterns = [
    path("applications/create/", ApplicationCreateView.as_view(), name="application-create"),
    path("contact/", ContactMessageCreateView.as_view(), name="contact-message"),
    path("admin-login/", AdminLoginView.as_view(), name="admin-login"),
    path("applications/list/", ApplicationListView.as_view(), name="application-list"),
]
