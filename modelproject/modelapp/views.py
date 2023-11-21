# candidate_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Candidatedirectory
from .forms import CandidateForm

def candidate_list(request):
    candidates = Candidatedirectory.objects.all()
    return render(request, 'candidate_app/candidate_list.html', {'candidates': candidates})

def candidate_detail(request, pk):
    candidate = get_object_or_404(Candidatedirectory, pk=pk)
    return render(request, 'candidate_app/candidate_detail.html', {'candidate': candidate})

def candidate_create(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('candidate_list')
    else:
        form = CandidateForm()
    return render(request, 'candidate_app/candidate_form.html', {'form': form})

def candidate_update(request, pk):
    candidate = get_object_or_404(Candidatedirectory, pk=pk)
    if request.method == 'POST':
        form = CandidateForm(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('candidate_list')
    else:
        form = CandidateForm(instance=candidate)
    return render(request, 'candidate_app/candidate_form.html', {'form': form})

def candidate_delete(request, pk):
    candidate = get_object_or_404(Candidatedirectory, pk=pk)
    candidate.delete()
    return redirect('candidate_list')
