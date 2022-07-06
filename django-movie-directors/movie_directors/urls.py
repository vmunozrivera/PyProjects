
from django.contrib import admin
from django.urls import path, include

import movies.urls

urlpatterns = [
    path('', include(movies.urls)),
    path('admin/', admin.site.urls)
]
