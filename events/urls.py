from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('events', views.all_events, name="list-events"),
    path('add_venue', views.add_venue, name="add-venue"),
    path('venues', views.list_venues, name="list-venues"),
    path('show_venue/<venue_id>', views.show_venue, name="show-venue"),
    path('search_venues', views.search_venues, name="search-venues"),
    path('update_venue/<venue_id>', views.update_venue, name="update-venue"),
]
