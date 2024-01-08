


from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register,name='register'),
    path('userinfo/',views.current_user,name='user_info'),
    path('userinfo/profile/',views.current_profile,name='current_profile'),
    path('userinfo/update',views.update_user,name='update_user'),
    path('get_all_users/',views.get_all_users,name='get_all_users')
]
