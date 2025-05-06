from django.urls import path
from users.views import UserSignUp, UserDetail, UserUpdate, UserDelete, UserLogin, UserLogout, ChangePassword

urlpatterns = [
    path('signup/', UserSignUp.as_view(), name='signup'),
    path('user_detail/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('user_update/<int:pk>/', UserUpdate.as_view(), name='user_update'),
    path('user_delete/<int:pk>/', UserDelete.as_view(), name='user_delete'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('change_password/<int:pk>/', ChangePassword.as_view(), name='change_password'),
]