from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'djangoapp'

urlpatterns = [
    # Path for login view
    path('login/', views.login_user, name='login'),

    # Add other routes as needed
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
