from django.shortcuts import render
from main.models import Post

# Create your views here.
def show_main(request):
	post_list = Post.objects.all().order_by('-created_at')
	return render(request, 'main/main.html', {'post_list':post_list})

def post_detail(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'main/post_detail.html', {'post':post,})