import openai
from django.shortcuts import render
from .models import Article
from django.conf import settings




def article_list(request):
    openai.api_key = settings.OPENAI_API_KEY
    query = request.GET.get('q')
    articles = Article.objects.all()

    if query:
        # Utilisation du modèle de langage pour augmenter la recherche
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=query,
            max_tokens=150
        )
        augmented_results = [result.text.strip() for result in response.choices]

        # Retourner les résultats augmentés
        return render(request, 'article_list.html', {'articles': articles, 'augmented_results': augmented_results})
    else:
        return render(request, 'article_list.html', {'articles': articles})


def chatbot(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        response = openai.Completion.create(
            engine="text-davinci-003", # Choisissez le modèle adapté à votre besoin
            prompt=question,
            max_tokens=150
        )
        answer = response.choices[0].text.strip()
    else:
        answer = None
    return render(request, 'chatbot.html', {'answer': answer})