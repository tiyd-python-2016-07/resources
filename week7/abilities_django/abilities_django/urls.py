from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from abilties import views


router = routers.DefaultRouter()
router.register(r'abilities', views.AbilityViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^', include('abilties.urls'))
]
