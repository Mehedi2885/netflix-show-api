from django.urls import path, include
from movie_show import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('name', views.MovieViewSet, basename='name')
"""path('country/<str:country>/', views.MovieInCountry.as_view()), for this url provide country as ""<Country>,<show_type>"""
urlpatterns = [
    path('summary/', views.Total_movie_tv_show.as_view()),
    path('country/<str:country>/', views.MovieInCountry.as_view()),
    path('', include(router.urls)),
]
