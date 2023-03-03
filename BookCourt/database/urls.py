from django.urls import path
from . import views


urlpatterns = [
    path('', views.katalog, name='katalog'),
    path('profile', views.profile, name='profile'),
    path('book/<int:book_id>', views.book, name='book'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
]