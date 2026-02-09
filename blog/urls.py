from django.urls import path
from .views import home_view, post_titles_view, WelcomeView

urlpatterns = [
    path('home/', home_view),
    path('posts/', post_titles_view),
    path('welcome/', WelcomeView.as_view()),
]
