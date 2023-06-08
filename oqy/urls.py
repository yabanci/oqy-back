from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='OQY API')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("oqy.core.infrastructure.api.urls")),
    path("auth/", include("oqy.auth.urls")),
    url(r'^$', schema_view),
]

# urlpatterns += docurls
