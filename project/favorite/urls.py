
from django.urls import path
from . import views

urlpatterns = [
    path('add_place_favorite/',views.add_place_favorite,name='add_place_favorite'),
    path('remove_place_favorite/<int:place_id>/',views.remove_place_favorite,name='remove_place_favorite'),
]