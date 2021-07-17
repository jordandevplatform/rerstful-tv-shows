from django.urls import path
from tvapp import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('shows/<int:theId>', views.showid),
    # path('new', views.new),
    path('shows', views.shows),
    path('shows/<int:theId>/edit', views.editShow),
    path('shows/<int:theId>/destroy', views.deleteshow),
    path('shows/<int:theId>/update', views.update)
]