from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from applications.security.views.auth import signin
from applications.security.views.home import ModuloTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ModuloTemplateView.as_view(), name='home'),
    path('security/', include('applications.security.urls', namespace='security')),
    path('auth/signin', signin, name='auth_signin'),
    path("__reload__/", include("django_browser_reload.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
