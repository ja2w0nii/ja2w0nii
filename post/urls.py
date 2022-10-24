from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'post'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/create/', views.post_create, name="post-create"),
    path('post/detail/<int:post_id>', views.post_detail, name='post-detail'),
]