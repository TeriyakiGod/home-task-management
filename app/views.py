from .models import Duty
from django.shortcuts import render, redirect
from .forms import DutyCreateForm, DutyChangeStatusForm, DutyEditForm, DutyChangePerson

def list_view(request):
    duties = Duty.objects.all()
    return render(request, 'list.html', {'duties': duties})

def list_rodzic_view(request):
    duties = Duty.objects.all()
    return render(request, 'list_rodzic.html', {'duties': duties})

def create_duty(request):
    if request.method == 'POST':
        form = DutyCreateForm(request.POST)
        if form.is_valid():
            duty = Duty()
            duty.name = form.cleaned_data['name']
            duty.status = 'Incomplete'
            duty.person = form.cleaned_data['person']
            duty.save()
            return redirect('list')
    else:
        form = DutyCreateForm()
    
    return render(request, 'create.html', {'form': form})

def change_status(request, duty_id):
    if request.method == 'POST':
        form = DutyChangeStatusForm(request.POST)
        if form.is_valid():
            duty = Duty.objects.get(pk=duty_id)
            duty.status = form.cleaned_data['status']
            duty.save()
            return redirect('list')
    else:
        form = DutyChangeStatusForm()

    return render(request, 'change_status.html', {'form': form})

def edit_or_delete_duty(request, duty_id):
    duty = Duty.objects.get(pk=duty_id)
    if request.method == 'POST':
        if 'edit' in request.POST:
            form = DutyEditForm(request.POST)
            if form.is_valid():
                duty.name = form.cleaned_data['name']
                duty.save()
                return redirect('list')
        elif 'delete' in request.POST:
            duty.delete()
            return redirect('list')
    else:
        form = DutyEditForm(initial={'name': duty.name})
    
    return render(request, 'edit_or_delete.html', {'form': form})

def assign_person_to_duty(request, duty_id):
    duty = Duty.objects.get(pk=duty_id)
    if request.method == 'POST':
        form = DutyChangePerson(request.POST)
        if form.is_valid():
            duty.person = form.cleaned_data['person']
            duty.save()
            return redirect('list')
    else:
        form = DutyChangePerson(initial={'person': duty.person})

    return render(request, 'assign_person.html', {'form': form})