from django.urls import path

from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.MovieView.as_view(), name='home'),
    path('<slug:slug>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review')
]
