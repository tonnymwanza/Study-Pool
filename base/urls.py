from django.urls import path
from . import views
from . views import FollowView
from . views import ProfileView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.login, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register' , views.register, name="register"),
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', ProfileView.as_view(), name='profile'),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
    path('update-user/', views.updateUser, name="update-user"),
    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),
    path('footer_page', views.footer_page, name="footer_page"),
    path('follow_func/<int:pk>/',FollowView.as_view(),  name='follow_func'),
    path('follow_func/<int:pk>/', views.follow_func, name='follow_func'),
    path('password_change', auth_views.PasswordChangeView.as_view(template_name="base/registration/password_change_form.html"), name="password_change"),
    path('password_change_done', auth_views.PasswordChangeDoneView.as_view(template_name="base/registration/password_change_done.html"), name="password_change_done"),
    path('password_reset', auth_views.PasswordResetView.as_view(template_name="base/registration/password_reset_form.html"), name="password_reset"),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name="base/registration/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="base/registration/password_reset_confirm.html"), name="password_reset_confirm"),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name="base/registration/password_reset_complete.html"), name="password_reset_complete"),
    path('testing', views.testing, name='texting'),
]
