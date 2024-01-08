
from django.urls import path
from . import views

urlpatterns = [
    path('get_states/',views.get_states,name='get_states'),
]