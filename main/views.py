from django.shortcuts import render
from main.models import Candidate


def index(request):
    candidates = Candidate.objects.all

    return render(request, 'index.html',
            {'candidates': candidates})
