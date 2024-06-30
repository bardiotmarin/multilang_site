from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL pour la page d'accueil (généralement en anglais)
    path('article_list/', views.article_list, name='article_list'),  # URL pour la liste des articles en français
    path('add/', views.add_article, name='add_article'),  # URL pour ajouter un article en français
    path('edit/<int:pk>/', views.edit_article, name='edit_article'),  # URL pour éditer un article en français
    path('chatbot/', views.chatbot_view, name='chatbot_view'),
    path('article_search/', views.article_search, name='article_search'),  # URL pour la recherche d'articles en français
    path('article_detail/<int:pk>/', views.article_detail, name='article_detail'),  # URL pour le détail d'un article en français
    path('delete/<int:pk>/', views.delete_article, name='delete_article'),  # URL pour supprimer un article en français
    path('rag_search/', views.rag_search, name='rag_search'),  # Ajout de l'URL pour la recherche RAG avec google et serp api
    path('get-unsplash-images/', views.get_unsplash_images, name='get_unsplash_images'),
    path('get-chat-history/', views.get_chat_history, name='get_chat_history'),
]