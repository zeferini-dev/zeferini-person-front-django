from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .services import person_service
from .forms import PersonForm


class PersonListView(View):
    """View for listing all persons."""
    
    def get(self, request):
        persons = person_service.list()
        return render(request, 'persons/list.html', {
            'persons': persons,
            'title': 'Pessoas'
        })


class PersonCreateView(View):
    """View for creating a new person."""
    
    def get(self, request):
        form = PersonForm()
        return render(request, 'persons/form.html', {
            'form': form,
            'title': 'Nova Pessoa',
            'is_edit': False
        })
    
    def post(self, request):
        form = PersonForm(request.POST)
        if form.is_valid():
            data = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email']
            }
            result = person_service.create(data)
            if result:
                messages.success(request, 'Pessoa criada com sucesso!')
                return redirect('person_list')
            else:
                messages.error(request, 'Erro ao criar pessoa. Tente novamente.')
        
        return render(request, 'persons/form.html', {
            'form': form,
            'title': 'Nova Pessoa',
            'is_edit': False
        })


class PersonEditView(View):
    """View for editing an existing person."""
    
    def get(self, request, person_id):
        person = person_service.get(person_id)
        if not person:
            messages.error(request, 'Pessoa não encontrada.')
            return redirect('person_list')
        
        form = PersonForm(initial={
            'name': person.get('name', ''),
            'email': person.get('email', '')
        })
        return render(request, 'persons/form.html', {
            'form': form,
            'title': 'Editar Pessoa',
            'is_edit': True,
            'person_id': person_id
        })
    
    def post(self, request, person_id):
        form = PersonForm(request.POST)
        if form.is_valid():
            data = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email']
            }
            result = person_service.update(person_id, data)
            if result:
                messages.success(request, 'Pessoa atualizada com sucesso!')
                return redirect('person_list')
            else:
                messages.error(request, 'Erro ao atualizar pessoa. Tente novamente.')
        
        return render(request, 'persons/form.html', {
            'form': form,
            'title': 'Editar Pessoa',
            'is_edit': True,
            'person_id': person_id
        })


class PersonDeleteView(View):
    """View for deleting a person."""
    
    def post(self, request, person_id):
        if person_service.delete(person_id):
            messages.success(request, 'Pessoa excluída com sucesso!')
        else:
            messages.error(request, 'Erro ao excluir pessoa. Tente novamente.')
        return redirect('person_list')
