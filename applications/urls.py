from django.urls import path
from applications.views import ApplicationCreateView, ContactMessageCreateView, AdminLoginView, ApplicationListView, UpdateApplicationStatusView, admin_overview

urlpatterns = [
    path("applications/create/", ApplicationCreateView.as_view(), name="application-create"),
    path("contact/", ContactMessageCreateView.as_view(), name="contact-message"),
    path("admin-login/", AdminLoginView.as_view(), name="admin-login"),
    path("applications/list/", ApplicationListView.as_view(), name="application-list"),
    path("applications/<int:pk>/update-status/", UpdateApplicationStatusView.as_view(), name="update-application-status"),
    path("admin-overview/", admin_overview, name="admin-overview")
]