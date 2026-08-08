from django.shortcuts import render
from django.http import JsonResponse
from .prompts import get_career_analysis
import json

def landing(request):
    return render(request, 'landing.html')

def analyze(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        skills = data.get('skills', '')
        interests = data.get('interests', '')
        goal = data.get('goal', '')

        result = get_career_analysis(skills, interests, goal)
        return JsonResponse(result)

    return JsonResponse({'error': 'Method not allowed'}, status=405)