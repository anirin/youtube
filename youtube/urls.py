from django.urls import path
from . import views

app_name = 'youtube'

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("detail/<int:video_id>/", views.detail, name="video"),
]