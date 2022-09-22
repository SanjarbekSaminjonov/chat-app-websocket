from django.contrib import admin
from django.urls import path, include
from app.views import SignUpView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', SignUpView.as_view(), name='signup'),
    path('', include('app.urls')),
]
