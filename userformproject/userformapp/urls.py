
from django.urls import path
from .views import user_form, user_form_list

urlpatterns = [
    path('user-form/', user_form, name='user_form'),
    path('user-form-list/', user_form_list, name='user_form_list'),
]
