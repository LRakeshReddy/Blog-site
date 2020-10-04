from django.urls import path
from . import views

app_name='blogsite'
urlpatterns=[
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('blogs/', views.Blogview.as_view(), name='blog'),
    path('logout/', views.logout, name='logout'),
    path('<int:user_id>/create/', views.create, name='create'),
    path('<int:user_id>/update/', views.update, name='update'),
    path('<int:blog_id>/edit/', views.edit, name='edit'),
    path('<int:blog_id>/deleteblog/', views.deleteblog, name='deleteblog'),
    path('<int:user_id>/deleteuser/', views.deleteuser, name='deleteuser'),
]