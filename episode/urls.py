from django.urls import path
from . import views

urlpatterns = [
    path('seasons', views.seasons, name='seasons'),
    path('episodes', views.episodes, name='episodes'),
    path('episode/<int:id>', views.episode, name = 'episode'),
    path('episode/prev/<int:id>', views.prev_episode, name = 'prev_episode'),
    path('episode/next/<int:id>', views.next_episode, name = 'next_episode'),
    path('casts', views.casts, name='casts'),
]

