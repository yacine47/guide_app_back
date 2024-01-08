
from django.urls import path
from . import views

urlpatterns = [
    path('get_reviews/',views.get_reviews,name='get_reviews'),
    path('delete_review/<int:id>/',views.delete_review,name='delete_review'),
    path('add_review_place/',views.add_review_place,name='add_review_place'),
    path('get_reviews_place/<int:id_place>',views.get_reviews_place,name='get_reviews_place'),
]