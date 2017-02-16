import django_tables2 as tables
from django_tables2.utils import A
from .models import Person

class PersonTable(tables.Table):
	edit = tables.LinkColumn('item_edit', text='Edit', args=[A('pk')], orderable=False,empty_values=())

	class Meta:
		model = Person

		attrs = {"class": "paleblue"}
