from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('post_details/', views.post_details, name='post-details'),
    path('tag/', views.tag, name='tag_list'),
    path('profile/', views.profile, name='profile')
]
