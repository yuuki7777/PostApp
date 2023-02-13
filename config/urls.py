from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
import accounts, articles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('articles/', include('articles.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #追加