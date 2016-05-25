from django.shortcuts import render, redirect
from main.models import Candidate
from main.forms import SubmissionForm


def index(request):
    if request.method=='POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            spl = Candidate.objects.get(name=form.cleaned_data["spl_candidates"])
            spl.votes += 1
            spl.save()
            aspl = Candidate.objects.get(name=form.cleaned_data["aspl_candidates"])
            aspl.votes += 1
            aspl.save()
            return redirect('aftermath')
    else:
        form = SubmissionForm()
        print form
    return render(request, 'index.html', {'form':form})


def aftermath(request):
    return render(request, 'aftermath.html')
