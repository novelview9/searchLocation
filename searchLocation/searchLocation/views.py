from django.http import JsonResponse
from django.shortcuts import render

def search_location(request):
    return render(request, 'location.html', {})

#    return JsonResponse({'foo':'bar'})
