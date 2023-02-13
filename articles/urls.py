from django.urls import path, include

from django.conf import settings 
from django.conf.urls.static import static
from articles import views

app_name = 'articles'
urlpatterns = [
    path('post/', views.PostView.as_view(), name='post'),
    path('home/', views.PostListView.as_view(), name='home'),
] 