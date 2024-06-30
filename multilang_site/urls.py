from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),  # URL pour gérer les langues
]

# Patterns d'URL internationalisés
urlpatterns += i18n_patterns(
    path('', include('main.urls')),  # Inclure les URLs de l'application 'main'
)

urlpatterns += [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)