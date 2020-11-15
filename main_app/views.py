import requests
from django.shortcuts import render


def api_posts(request):
   response = requests.get('https://jsonplaceholder.typicode.com/posts/')
   # transfor the response to json objects
   posts = response.json()
   return render(request, "home.html", {"posts": posts})


def post_details(request,post_id):
   response = requests.get('https://jsonplaceholder.typicode.com/posts/{post_id}')
   # transfor the response to json objects
   posts = response.json()
   return render(request, "details.html", {"posts": posts})

