from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('user/toggle-block/<int:user_id>/', views.toggle_block, name='toggle_block'),
    path('user/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('manage-notes/', views.manage_notes, name='manage_notes'),
    path('note/approve/<int:note_id>/', views.approve_note, name='approve_note'),
    path('note/reject/<int:note_id>/', views.reject_note, name='reject_note'),
    path('view-messages/', views.view_messages, name='view_messages'),
]
