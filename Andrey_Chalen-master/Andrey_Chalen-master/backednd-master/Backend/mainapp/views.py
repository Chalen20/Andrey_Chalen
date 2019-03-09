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
def about(request):
    return render(request, 'about.html')
def rules(request):
    return  render(request, 'rules.html')
def advertice(request):
    return  render(request, 'advertice.html')
def developer(request):
    return render(request, 'developer.html')
def recover(request):
    return render(request, 'recover.html')



