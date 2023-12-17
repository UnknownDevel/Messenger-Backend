from django.urls import path
from django.contrib.auth import views as authviews
from . import views

urlpatterns = [
    path('', views.page, name='page'),
    path('signup/', views.signup, name='signup'),
    path('login/', authviews.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', authviews.LogoutView.as_view(), name='logout')
]