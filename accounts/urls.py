from django.urls import path, include

from django.conf import settings 
from django.conf.urls.static import static
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('signup/', views.UserSignUpView.as_view(), name='signup'),
    path('login/', views.LogInView.as_view(), name='login'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
] 