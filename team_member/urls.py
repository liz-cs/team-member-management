from django.urls import path

from team_member import views

app_name = 'team_member'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.EditView.as_view(), name='edit'),
    path('add/', views.add, name='add'),
    path('add_save/', views.add_save, name='add_save'),
    path('<int:member_id>/edit', views.edit_save, name='edit_save'),
    path('<int:member_id>/delete', views.delete, name='delete'),
]