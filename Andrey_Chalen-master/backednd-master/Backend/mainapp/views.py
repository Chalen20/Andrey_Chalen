from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "wrapper.html")
def registr(request):
    return render(request, "registr.html")
def reset(request):
    return render(request, 'reset.html')
def example(request):
    return render(request, 'example.html')





