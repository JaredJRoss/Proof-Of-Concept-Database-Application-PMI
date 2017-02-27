import django_filters
from .models import Person


class PersonListFilter(django_filters.FilterSet):

  class Meta:
    model = Person
    fields =  '__all__'
    order_by = ['pk']