from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Include hospital app URLs first
    path('', include('hospital.urls')),

    # Redirect root '/' to department list
    # Only triggers if root URL '/' is accessed
    path('', RedirectView.as_view(pattern_name='department_list', permanent=False)),
]
