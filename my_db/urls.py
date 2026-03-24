from django.contrib import admin
from django.urls import path
from myapp.views import homepage,noutbokpage
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name='home'),
    path('noutbooks/',noutbokpage,name='noutbooks')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)