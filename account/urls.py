from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import register, profile, UserUpdate

app_name = 'account'
urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    # path('<int:pk>/update/', UserUpdate.as_view(), name='update'),
    path('login/', LoginView.as_view(template_name="account/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="account/logout.html"), name='logout')
]