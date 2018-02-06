from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from os import listdir
from os.path import isfile, join
from articlesapp.helpers import util
from polls.models import Article
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

ARTICLES_PATH = 'articles'

def main(request):
   return render(request, "main.html", {})

@csrf_exempt
def uploadArticle(request):
   if request.method == 'POST':
      articleName = request.POST['name']
      description = request.POST['description']
      newArticle = request.FILES['file']
      with open('articles/'+newArticle.name, 'wb+') as destination:
         for chunk in newArticle.chunks():
            destination.write(chunk)

      if not Article.objects.filter(articleName=articleName):
         article = Article(articleName=articleName, rating=0, fileName = newArticle.name, description = description)
         article.save()

   return render(request, "main.html", {})

@login_required()
def articlesList(request):
   articles = Article.objects.all()
   return render(request, "articles.html", { 'articles' : articles})

@login_required()
def article(request, articleName):
   with open(ARTICLES_PATH+'/'+articleName, 'rb') as pdf:
      response = HttpResponse(pdf.read(), content_type='application/pdf')
      response['Content-Disposition'] = 'inline;filename=test.pdf'
      return response

@login_required()
def articleCard(request, articleName):
   article = None
   if Article.objects.filter(articleName=articleName):
      article = Article.objects.filter(articleName=articleName)[0]
   return render(request, "articleCard.html", {'filename' : article.fileName, 'articleName' : article.articleName, 'rating' : article.rating, 'description' : article.description })

@csrf_exempt
def submitVote(request):
   ratingValue = request.POST['ratingValue']
   articleName = request.POST['articleName']
   article = Article.objects.filter(articleName=articleName)[0]
   article.rating = int(ratingValue)
   article.save()
   return HttpResponse("voted")

@login_required()
def redirectGuest(request):
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)