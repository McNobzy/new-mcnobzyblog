from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.create, name='create'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('author/<str:pk>/<str:name>', views.postAuthor, name='postAuthor'),
    path('post/<str:pk>', views.viewPost, name='post'),
    path('edit/<str:pk>/', views.edit_post, name='edit'),
    path('edit-profile/<str:pk>', views.edit_profile, name='edit-profile'),
    path('profile/<str:name>', views.profile, name='profile'),
    path('search/', views.search, name='search'),
    path('delete/<str:pk>', views.delete, name="delete")
    # path('edit/<str:pk>/<str:func>', views.editPost, name="editPost")
]