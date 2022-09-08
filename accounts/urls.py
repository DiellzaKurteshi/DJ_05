from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name = 'signup'),  #shkaku i .as_view e kemi class
]