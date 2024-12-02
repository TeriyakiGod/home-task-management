from django import forms
from .models import Person

class DutyCreateForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    person = forms.ModelChoiceField(queryset=Person.objects.all(), label='Person', required=False)

class DutyChangeStatusForm(forms.Form):
    status = forms.ChoiceField(choices=(('Incomplete', 'Incomplete'), ('Complete', 'Complete')), label='Status')

class DutyEditForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)

class DutyChangePerson(forms.Form):
    person = forms.ModelChoiceField(queryset=Person.objects.all(), label='Person')