from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def post_details(request):
    return render(request, 'main/post_details.html')

def tag(request):
    return render(request, 'main/tag.html')

def profile(request):
    return render(request, 'main/profile.html')
    

