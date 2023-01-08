from .  import views
from django.urls import path

urlpatterns = [
    path('register/', views.register_user, name='user_register' ),
     path('login/', views.login, name='login' ),
    path('me/', views.current_user_detail, name='current_user_detail' ),
]  