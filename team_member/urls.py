from django.urls import path

from team_member import views

app_name = 'team_member'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.add, name='add'),
    path('<int:member_id>/edit', views.edit, name='edit'),
    path('<int:member_id>/delete', views.delete, name='delete')
]
