from django.shortcuts import render

def news(request):
    context = {}
    return render(request, "post/news.html")
