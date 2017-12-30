from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

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

