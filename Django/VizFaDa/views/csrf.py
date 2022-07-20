from django.shortcuts import render

def get_csrf(request):
    return render(request, 'csrf.html')