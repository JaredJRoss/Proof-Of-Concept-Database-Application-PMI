from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Person
from django.template import loader
from django.http import Http404
from django.forms import ModelForm
#from .models import PersonForm
from .forms import PersonForm
from .tables import PersonTable
from django_tables2 import RequestConfig
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic import TemplateView
from django_tables2 import SingleTableView




# Create your views here.

#Don't worry about this one. 
def index(request):
	table = PersonTable(Person.objects.all())
	context = {
		'table': table,

	}

	RequestConfig(request).configure(table)
	return render(request, 'ogdb/person_list.html', context)

#TGENERATES MAIN PAGE. TABLE. 
@login_required
def person_list(request):
	table = PersonTable(Person.objects.all())
	context = {
		'table': table,
	}

	RequestConfig(request).configure(table)
	return render(request, 'ogdb/person_list.html', context)

#not in current use. will be used as a Constituent Details Page
@login_required
def detail(request, person_id):
	try:
		person = Person.objects.get(pk=person_id)
	except Person.DoesNotExist:
		raise Http404("Employee does not exist")
	return render(request, 'ogdb/detail.html', {'employee': person})

@login_required
def add_new(request):
	form = PersonForm(request.POST or None);
	context = {
		'form' : form
	}
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/ogdb/home')


	return render(request, 'ogdb/new_person.html', context)

#Editing page
@login_required
def item_edit(request, person_id):
	instance = get_object_or_404(Person, id=person_id)
	form = PersonForm(request.POST or None, instance=instance)
   

	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/ogdb/home')
	context = {
		'form' : form,
		'pk' : person_id
	}

    
	return render(request, 'ogdb/item_edit.html', context)

#Delete Person confirm page
class personDelete(DeleteView):
	model = PersonForm
	success_url = reverse_lazy('home')
	template_name = 'ogdb/person_confirm_delete.html'

from .filters import PersonListFilter
from .forms import PersonListFormHelper

class PersonListView(TemplateView):
    template_name = 'ogdb/person_list_2.html'

    def get_queryset(self, **kwargs):
        return Person.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PersonListView, self).get_context_data(**kwargs)
        filter = PersonListFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        filter.form.helper = PersonListFormHelper()
        table = PersonTable(filter.qs)
        RequestConfig(self.request).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context






