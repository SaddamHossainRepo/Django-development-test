from django.urls import path
from .views import api_posts, post_details

app_name = 'main_app'


urlpatterns = [
    path('', api_posts, name="api_list"),
    path('<post_id>', post_details, name="post_details"),
    # path('<int:post_id>', post_details),
]
