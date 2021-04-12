from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    #path("characters/", views.aux, name="aux"),
    path("breakingbad/<int:s>/", views.bbad, name="bbad"),
    path("bettercallsaul/<int:s>/", views.bcsaul, name="bcsaul"),
    path("episodes/<int:id>/", views.episodes, name="episodes"),
    path("characters/<int:cid>/", views.characters, name="characters")
]