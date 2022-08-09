from .import views
from django.urls import path

urlpatterns=[
    path('', views.index, name='index'),
    # inke dar kudum az post ha joda ba asase shomare namayesh dade beshe
    path('<int:post_id>', views.detail, name='detail'),
]