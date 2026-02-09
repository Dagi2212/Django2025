from django.http import HttpResponse
from django.views import View
from .models import Post


# Question 2
def home_view(request):
    return HttpResponse("Hello Blog")


# Question 5

def post_titles_view(request):
    posts = Post.objects.all()

    output = ""
    for post in posts:
        output += f"""
        <h2>{post.title}</h2>
        <p>{post.content}</p>
        <small>Published on: {post.published_date}</small>
        <hr>
        """

    return HttpResponse(output)


# Question 4 (CBV)
class WelcomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to Django CBV")
