import os
import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from .models import Article
from .form import ArticleForm
from serpapi import GoogleSearch

from dotenv import load_dotenv
import google.generativeai as genai

# Load the .env file
load_dotenv()

# Accéder aux variables d'environnement
UNSPLASH_ACCESS_KEY = os.getenv('UNSPLASH_ACCESS_KEY')

# Gemin clé d'API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Init modèle Gemini Pro ( Free tiers api)
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])


# CRUD Operations

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    next_article = Article.objects.filter(pk__gt=pk).order_by('pk').first()
    
    context = {
        'article': article,
        'next_article': next_article
    }
    
    return render(request, 'article_detail.html', context)


def article_search(request):
    query = request.GET.get('query', '')
    if query:
        articles = Article.objects.filter(title__icontains=query)
    else:
        articles = Article.objects.all()  # Afficher tous les articles si aucune recherche n'est effectuée
    return render(request, 'home.html', {'articles': articles})



def article_list(request):
    articles = Article.objects.all()
    augmented_results = [...]  # Placeholder for additional data if needed
    return render(request, 'article_list.html', {'articles': articles, 'augmented_results': augmented_results})



def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'redirect_url': '/article_list/'})  # Remplacez par votre URL d'affichage des articles
    else:
        form = ArticleForm()
    
    return render(request, 'add_edit_article.html', {'form': form})


def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return JsonResponse({'redirect_url': reverse('article_list')})
    else:
        form = ArticleForm(instance=article)

    return render(request, 'add_edit_article.html', {'form': form})


def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    
    if request.method == 'POST':
        article.delete()
        return redirect('home')
    
    return render(request, 'delete_article.html', {'article': article})


# home 
def home(request):
    articles = Article.objects.all()
    return render(request, 'home.html', {'articles': articles})



# Chatbot gemini *********

# This will store chat history for each session user
chat_history_dict = {}

def chatbot_view(request):
    global chat_history_dict

    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        session_key = request.session.session_key

        if session_key not in chat_history_dict:
            chat_history_dict[session_key] = []

        # Store the user input in the chat history
        chat_history_dict[session_key].append({'sender': 'user', 'text': user_input})

        # Envoyer la question à Gemini Pro et obtenir la réponse
        response = chat.send_message(user_input, stream=True)
        bot_response = "\n".join([chunk.text for chunk in response])

        # Store the bot response in the chat history
        chat_history_dict[session_key].append({'sender': 'bot', 'text': bot_response})

        return JsonResponse({'response': bot_response})

    return render(request, 'chatbot.html')

def get_chat_history(request):
    session_key = request.session.session_key

    if session_key in chat_history_dict:
        chat_history = chat_history_dict[session_key]
    else:
        chat_history = []

    return JsonResponse(chat_history, safe=False)


# RAG (Retrieval-Augmented Generation) Search with SerpApi

def rag_search(request):
    query = request.GET.get('query')
    results = []
    current_language = request.LANGUAGE_CODE  # Get the current language from the request

    if query:
        params = {
            "q": query,
            "hl": current_language,
            "gl": current_language,
            "api_key": os.getenv('SERPAPI_API_KEY'),  # Use the API key from environment variables
        }
        client = GoogleSearch(params)
        results = client.get_dict().get("organic_results", [])

    context = {
        'query': query,
        'results': results,
    }
    
    return render(request, 'rag_search.html', context)


# Fetch images from Unsplash

def get_unsplash_images(request):
    search_query = request.GET.get('search_query', 'nature')  # Utilisez 'nature' par défaut si aucune recherche n'est spécifiée
    url = 'https://api.unsplash.com/search/photos/'
    params = {
        'query': search_query,
        'per_page': 10,  # Nombre d'images à retourner par page
        'client_id': os.getenv('UNSPLASH_ACCESS_KEY')
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()['results']
        image_options_html = ''
        for image in data:
            image_url = image['urls']['regular']
            image_options_html += f'<option value="{image_url}">{image_url}</option>'

        return JsonResponse(image_options_html, safe=False)

    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=response.status_code)