from django import forms
from jobs.models import Job


class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location', 'job_type', 'category', 'description']
        widgets = {'job_type': forms.RadioSelect}