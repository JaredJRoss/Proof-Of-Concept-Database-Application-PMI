from django import forms
from .models import Person
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import InlineField, FormActions, StrictButton


class PersonForm(forms.ModelForm):

    class Meta:

        model = Person
        fields = '__all__'

class PersonListFormHelper(FormHelper):    
    form_method = 'GET'
    field_template = 'bootstrap3/layout/inline_field.html'
    field_class = 'col-xs-3'
    label_class = 'col-xs-3'
    layout = Layout(
    	 Fieldset(
                    '<i class="fa fa-search"></i> Search Constituent Records',       
                	InlineField('resource_first_name'),
                    InlineField('resource_last_name'),
                    'HUBzone',
                    'employment_status',
                ),
    			#'resource_first_name',
             	#'resource_last_name',
             	#'HUBzone',
             	#'employment_status',
              Submit('submit', 'Apply Filter'),
    )