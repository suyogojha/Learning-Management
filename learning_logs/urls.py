"""Defines url patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),

    # Show all topics.
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Page for a user to add a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for a user to add an entry to a topic.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Page for a user to edit an entry.for
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

    # Page for deleting an entry.
    path('delete_entry/<int:entry_id>', views.delete_entry, name='delete_entry'),
]