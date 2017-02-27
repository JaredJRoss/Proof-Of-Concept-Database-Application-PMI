from django.conf.urls import url
from .models import Person
from . import views

urlpatterns = [
    url(r'^$', views.person_list, name='index'),
    url(r'^(?P<person_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^home/$', views.person_list, name= 'home'),
    url(r'^new_person/$', views.add_new, name= 'add'),
    url(r'^edit/(?P<person_id>\d+)/$', views.item_edit, name='item_edit'),
    url(r'^delete/(?P<pk>\d+)/$', views.personDelete.as_view(model = Person), name="person_delete"),
    url(r'^test/$', views.PersonListView.as_view(), name="person_list_2"),




]