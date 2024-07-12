
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.tweet_list,name="tweet_list"),
    path('create/',views.tweet_create,name="tweet_create"),
    path('<int:tweet_id>/edit',views.tweet_edited,name="tweet_edited"),
    path('<int:tweet_id>/delete',views.tweet_delete,name="tweet_delete"),
    path("register/",views.register_user,name='register')

]