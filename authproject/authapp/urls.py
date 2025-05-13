from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    #path('authapp/signup/', views.signup, name='signup'),
    # path('authapp/signup/done/', views.signupDone, name='signup_done'),
    path('login/', views.login, name='login'),
    #path('authapp/logout/', views.logout, name='logout'),  
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),  
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view, name='password_change_done'),
    #path('authapp/password_reset/', views.passwordReset, name='password_reset'),
    #path('authapp/password_reset/done/', views.passwordResetDone, name='password_reset_done'),
    #path('authapp/reset/<uidb64>/<token>/', views.passwordResetConfirm, name='password_reset_confirm'),
    #path('authapp/reset/done/', views.passwordResetComplete, name='password_reset_complete'),
]
