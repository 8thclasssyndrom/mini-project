from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from main.views import CardListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', CardListView.as_view(), name="home")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
