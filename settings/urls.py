from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tfa.urls')),
    path('', include('csvapp.urls')),
    path('', include('djorm.urls')),
    path('', include('pypdf.urls')),
    path('', include('pychartjs.urls')),
    path('', include('pyqrcodeapp.urls')),
    path('', include('pyasync.urls')),
    path('', include('dj_dropzone.urls')),
    path('', include('djs.urls')),
    path('', include('bulkcrud.urls')),
    path('', include('import_export_app.urls')),
    path('estates/', include('estates.urls')),
    path('report/', include('report.urls')),
    path('events/', include('events.urls')),
    path('imgcrop/', include('imgcrop.urls')),
    path('thread/', include('py_threading.urls')),
    path('multistepform/', include('multistepform.urls')),
    path('', include('editorjsapp.urls')),
    path('', include('ajaxcrud.urls')),
    path('', include('data_visualize.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('silk/', include('silk.urls', namespace='silk'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)