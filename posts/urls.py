from django.urls import path
from posts.views import posts, post_details

app_name = 'posts'


urlpatterns = [
    path('', posts, name="list"),
    path('<int:id>', post_details),
]
