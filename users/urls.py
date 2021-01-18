from django.urls import path
from .views import SignUpView,ChangePasswordView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),

]