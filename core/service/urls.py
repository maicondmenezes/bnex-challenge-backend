"""
URL configuration for service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from accounts.views import CustomAuthToken, ListUsers
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from products.views import ProductViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

router = DefaultRouter()
router.register(r'products', ProductViewSet)
schema_view = get_schema_view(
    title='Products API',
    description='API for products management',
    version='0.1.0',
    public=True,
)
swagger_view = TemplateView.as_view(
    template_name='docs-swagger.html', extra_context={'schema_url': 'schema'}
)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api/', include(router.urls)),
    path('api/users/', ListUsers.as_view(), name='user-list'),
    path('api/schema/', schema_view, name='schema'),
    path('api/auth/token/', CustomAuthToken.as_view(), name='auth-token'),
    path('api/docs/swagger/', swagger_view, name='docs-swagger'),
]
