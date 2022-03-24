from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('topic_detail/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('topic_list/', views.topic_list, name='topic_list'),
    path('post_detail/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post_list/', views.post_list, name='post_list'),
    path('topic_post_list/<int:topic_id>/', views.topic_post_list, name='topic_post_list'),
    path('add_topic/', views.add_topic, name='add_topic'),
    path('edit_topic/<int:topic_id>/', views.edit_topic, name='edit_topic'),
    path("register_user/", views.register_user, name="register_user"),
    path("login_user/", views.login_user, name="login_user"),
    path("logout_user/", views.logout_user, name="logout_user"),
    path('add_post/<int:topic_id>/', views.add_post, name='add_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),

]
