import django_tables2 as tables
from django_tables2.utils import A
from .models import Person

class PersonTable(tables.Table):
	edit = tables.LinkColumn('item_edit', text='Edit', args=[A('pk')], orderable=False,empty_values=())

	def render_name(self, value, record):
		url = record.get_absolute_url()
		return mark_safe('<a href="%s">%s</a>' % (url, record))

	class Meta:
		model = Person

		attrs = {"class": "table-striped table-bordered"}
		empty_text = "There are no customers matching the search criteria..."
