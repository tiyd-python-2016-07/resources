from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tasks/', include('tasks.urls')),
    url(r'^example/', include('tasks.urls'))
]
