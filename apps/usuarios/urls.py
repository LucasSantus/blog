from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from .views import *
from .validate import *

urlpatterns = [
    path('accounts/', include([
        # PROFILE
        path('profile/', profile, name="profile"),

        # DESCRIPTION
        path('<slug:slug_user>/', include([
            path('description/', description_user, name="description_user"),
        ])),

        #SIGN UP
        path('signup/', SignUpView.as_view(), name='signup'),

        #LOGIN
        path('login/', auth_views.LoginView.as_view(template_name="usuarios/login/login.html"), name="login"),

        #LOGOUT
        path("logout/", auth_views.LogoutView.as_view(template_name="usuarios/logout/logout.html"), name="logout"),
        
        #RESET PASSWORD
        path('password/reset/', include([
            path('sent/', auth_views.PasswordResetDoneView.as_view(template_name="usuarios/reset_password/reset-password-done.html"), name="password_reset_done"),
            path('<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="usuarios/reset_password/reset-password-confirm.html"), name="password_reset_confirm"),
            path('complete/', auth_views.PasswordResetCompleteView.as_view(template_name="usuarios/reset_password/reset-password-complete.html"), name="password_reset_complete"),
            path('', auth_views.PasswordResetView.as_view(template_name="usuarios/reset_password/reset-password.html"), name="reset_password"),
        ]))
    ])),

    # VALIDATE
    path('validate/', include([
        path('email/', validate_email, name='validate_email'),
        path('user/', validate_user, name='validate_user'),
        path('email-registered/', validate_email_registered, name='validate_email_registered'),
    ]))
]