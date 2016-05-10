from django import forms
from main.models import Candidate


class SubmissionForm(forms.Form):
    name = forms.CharField(max_length=100)
    spl_candidates = forms.ModelChoiceField(queryset=Candidate.objects.filter(category="SPL"),
                                            widget=forms.RadioSelect,
                                            empty_label=None)
    aspl_candidates = forms.ModelChoiceField(queryset=Candidate.objects.filter(category="ASPL"),
                                             widget=forms.RadioSelect,
                                             empty_label=None)
