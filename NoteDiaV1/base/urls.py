from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView

urlpatterns = [ 
    path('login/',views.loginPage,name="login"),
    path('create-topic/', views.createTopic, name='create-topic'),
    path('register/',views.registerPage,name="register"),
    path('logout/',views.logoutUser,name="logout"),
    path('',views.Home,name="home"),
    path('profile/<str:pk>/',views.userProfile,name="user-profile"),
    path('room/<str:pk>/',views.room,name="room"),
    path('create-room/',views.createRoom,name="create-room"),
    path('create-room-media/',views.createRoomMedia,name="create-room-media"),
    path('Update-Room/<str:pk>/',views.updateRoom,name="update-room"),
    path('Delete-Room/<str:pk>/',views.deleteRoom,name="delete-room"),
    path('Delete-message/<str:pk>/',views.deleteMessage,name="delete-message"),
    path('update-user/',views.updateUser,name="update-user"),
    path('topics/',views.topicsPage,name="topics"),
    path('activity/',views.activityPage,name="activity"),
    path('User-Topics/',views.choose_topics,name="user-topics"),
    path('reset-password/<str:pk>/',views.UserResetPassword,name="reset-password"),
    path('password-reset/', PasswordResetView.as_view(template_name='registration/forgot_password.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/forgot_password_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/forgot_password_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/forgot_password_complete.html'), name='password_reset_complete'),
]