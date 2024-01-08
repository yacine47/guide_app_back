
from django.urls import path
from . import views

urlpatterns = [
    path('get_places/',views.get_places,name='get_places'),
    path('get_categories/',views.get_categories,name='get_categories'),
    path('get_places_favorite/',views.get_places_favorite,name='get_places_favorite'),
    path('add_place_with_images/',views.add_place_with_images,name='add_place_with_images'),
]