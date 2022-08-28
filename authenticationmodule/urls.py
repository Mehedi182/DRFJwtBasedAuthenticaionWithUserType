from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Django Authentication",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.ourapp.com/",
        contact=openapi.Contact(email="contact@test.local"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [

    #Authentication
    path('token/',
         jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('hello/', views.HelloView.as_view(), name='hello'),

    path('user/', views.UserList.as_view()),
    path('user_registration/', views.CreateUserView.as_view()),


    path('docs/', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),

    path('api/api.json/', schema_view.without_ui(cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',cache_timeout=0), name='schema-redoc'),
]
