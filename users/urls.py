from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from . import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('register/', views.register_user, name='register'),
    path('password-reset', PasswordResetView.as_view(template_name='users/reset.html'), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='users/confirm_reset.html'), name='password_reset_confirm'),
    path('password-reset-done', PasswordResetDoneView.as_view(template_name='users/reset_done.html'), name='password_reset_done'),
    path('password-reset-complete', PasswordResetCompleteView.as_view(template_name='users/reset_complete.html'), name='password_reset_complete'),
]
