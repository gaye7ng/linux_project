from django.shortcuts import render

# Create your views here.
def dash1(request):
    return render(request, 'board/dash1.html')