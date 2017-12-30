from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from os import listdir
from os.path import isfile, join
from articlesapp.helpers import util

ARTICLES_PATH = 'articles'

def main(request):
   return render(request, "main.html", {})

@csrf_exempt
def uploadArticle(request):
   if request.method == 'POST':
      print("upload file")
      print(request.FILES['pdfFile'])

      newArticle = request.FILES['pdfFile']
      with open('articles/'+newArticle.name, 'wb+') as destination:
         for chunk in newArticle.chunks():
            destination.write(chunk)

   return render(request, "main.html", {})

def articlesList(request):
   onlyfiles = [f for f in listdir(ARTICLES_PATH) if isfile(join(ARTICLES_PATH, f))]
   names = util.normalizeNames(onlyfiles)
   return render(request, "articles.html", { 'articles' : names})

def article(request, articleName):
   with open(ARTICLES_PATH+'/'+articleName, 'rb') as pdf:
      response = HttpResponse(pdf.read(), content_type='application/pdf')
      response['Content-Disposition'] = 'inline;filename=test.pdf'
      return response

