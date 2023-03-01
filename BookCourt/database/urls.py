from django.urls import path
from . import views


urlpatterns = [
    path('', views.katalog, name='katalog'),
    path('create', views.import_data_to_db, name='create'),
    path('profile', views.profile, name='profile'),
    path('homepagea', views.home_page, name='homepagea')
]