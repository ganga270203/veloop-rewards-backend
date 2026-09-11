from django.urls import path

from .views import ScoreListView

from .views import (GameListView,GameDetailView,ScoreListView,LoginView, RegisterView,)


urlpatterns = [

    path( "games/",GameListView.as_view(),name="games"),

    path( "games/<int:pk>/",GameDetailView.as_view(),name="game-detail"),

    path("scores/",ScoreListView.as_view(),name="scores"),

    path("login/",LoginView.as_view(),name="login"),

    path("register/",RegisterView.as_view(),name="register"),

]