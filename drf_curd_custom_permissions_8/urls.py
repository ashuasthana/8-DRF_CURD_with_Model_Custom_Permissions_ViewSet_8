"""drf_curd_custom_permissions_8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from rest_framework.authtoken import views as view
from django.contrib import admin
from django.urls import path, include
from testapp import views
from rest_framework import routers
router = routers.DefaultRouter()
# router.register('api',views.EmployeeModelViewSetCBV,basename='api')
router.register('api', views.EmployeeModelViewSetCBV)
# for authentication 'rest_framework.authtoken' modules 'views' imported


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('get-api-token/', view.obtain_auth_token, name='get-api-token')

]
