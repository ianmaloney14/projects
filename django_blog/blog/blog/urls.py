from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_blog.urls')),
    path('login_reg/', include('django.contrib.auth.urls')),
    path('login_reg/', include('login_reg.urls')),
]
