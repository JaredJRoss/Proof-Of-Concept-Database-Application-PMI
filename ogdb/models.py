from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils.translation import gettext as _
from django.forms import ModelForm
#from django_filters import rest_framework as filters



# USE THIS TO ENABLE SCROLL DOWN SELECTION
TITLE_CHOICES = (
    ('TI', 'Technical Intern'), 
    ('NTI', 'Non-Technical Intern'),
    ('SUP', 'Supervisior'), 
    ('DON', 'Donor'),
    ('FTE', 'Full-Time Employee'),
    ('NA', 'N/A'),
)
STATUS = (
	('C', 'Current'),
	('F', 'Former'),
	('L', 'Leave'),
	)
BILL = (
	('B', 'Billable'),
	('N', 'Non-Billable'),
	)

# Create your models here.

#class Person(models.Model):
#	person_lastname = models.CharField(_("Last Name"), max_length=20)
#	person_firstname = models.CharField(_("First Name"), max_length=20)
	#SCROLL DOWN USES choices
#	person_title = models.CharField(max_length=19, choices=TITLE_CHOICES)
#	person_date = models.DateField(_("Start Date"), default=datetime.date.today)

"""
	def __unicode__(self):
		name = []
		name.append(self.person_lastname)
		name.append(", ")
		name.append(self.person_firstname)
		return  ''.join(name)
"""



class Person(models.Model):
	recruitment_source = models.CharField(_("Recruitment Source"), max_length = 100, default = "N/A")
	responsible_recruiter = models.CharField(_("Responsible Recruiter"), max_length = 100, default = "N/A")
	status = models.CharField(_("Status"), max_length = 50, default = "N/A")
	clock_sequence = models.CharField(_("Clock Sequence"), max_length = 100, default = "N/A")
	resource_last_name = models.CharField(_("Resource Last Name"), max_length = 100, default = "N/A")
	resource_first_name = models.CharField(_("Resource First Name"), max_length = 100, default = "N/A")
	date_of_hire = models.DateField(_("Date of Hire"), default=datetime.date.today)
	HUBzone = models.BooleanField(_("HUBzone"), default = True)
	resource_type = models.CharField(_("Resource Type"), max_length = 100, default = "N/A")
	payroll_company = models.CharField(_("Payroll Company"), max_length = 100, default = "N/A")
	probationary_end= models.DateField(_("Probationary End"), default=datetime.date.today)
	supervisor_name = models.CharField(_("Supervisor Name"), max_length = 100, default = "N/A")
	resource_email = models.CharField(_("Resource Email"), max_length = 100, default = "N/A")
	home_address = models.CharField(_("Home Address"), max_length = 100, default = "N/A")
	resource_telephone = models.CharField(_("Resource Personal Telephone"), max_length = 100, default = "000-000-0000")
	employment_status = models.CharField(_("Employment Status"), max_length = 50, choices=STATUS, default = "N/A")
	PMI_career_title = models.CharField(_("PMI Career Title    "), max_length = 100, default = "N/A")
	department = models.CharField(_("Department/Project Assigned"), max_length = 100, default = "N/A")
	project_title = models.CharField(_("Project/Functional Title"), max_length = 100, default = "N/A")
	contract_labor = models.CharField(_("Contract Labor Category"), max_length = 100, default = "N/A")
	GSA_labor = models.CharField(_("GSA Labor Category"), max_length=100, default = "N/A")
	billable = models.CharField(_("Billable/Non-Billable"), max_length=50, choices=BILL, default = "N/A")
	GSA_vehicle = models.CharField(_("GSA Vehicle"), max_length = 100, default = "N/A")
	work_location = models.CharField(_("Work Location"), max_length=100, default = "N/A")
	hourly_pay = models.IntegerField(_("Hourly Pay Rate"), max_length=50, default = 0)
	GSA_rate = models.CharField(_("GSA Rate"), max_length = 100,default = "N/A")
	discount = models.IntegerField(_("Discount (%)"), max_length=50, default = 0)
	client_bill = models.CharField(_("Client Bill Rate"), max_length = 100,default = "N/A")
	comments = models.CharField(_("Comments (Task Codes, Invoicing POC, COI)"), max_length = 400,default = "N/A")
	offer_sent = models.BooleanField(_("Offer/Contract Sent"), default = True)
	clock_sequence = models.IntegerField(_("Clock Sequence"), max_length = 50, default = 0)
	offer_contract = models.CharField(_("Offer Contract/NDA FE"), max_length = 100, default = "N/A")
	campin = models.BooleanField(_("CAMPIN Sent to Candidate"), default = True)
	clearance_packet = models.BooleanField(_("Clearance Packet Complete"), default = True)
	clearance_packet_sent = models.BooleanField(_("Completed Clearance Packet Sent to JA"), default = True)
	clearance_packet_submitted = models.BooleanField(_("Clearance Packet Submitted to Census"), default = True)
	cleared_date = models.DateField(_("Cleared Date"), default=datetime.date.today)
	commission_logged = models.BooleanField(_("Commission Logged?"), default = True)
	commission_due = models.DateField(_("Commission Due Date"), default=datetime.date.today)
	PMI_email = models.CharField(_("PMI Email"), max_length = 100, default = "N/A")
	google_groups = models.CharField(_("Google Groups"), max_length=100, default = "N/A")
	toolkit = models.CharField(_("Toolkit"), max_length=100, default = "N/A")
	paycom_login = models.CharField(_("Paycom Login"), max_length=100, default = "N/A")
	efaact = models.CharField(_("eFAACT"), max_length=100, default = "N/A")
	computer = models.CharField(_("Computer"), max_length=100, default = "N/A")
	software_r = models.CharField(_("Software Requests"), max_length=400, default = "N/A")
	gb_security_r = models.CharField(_("GB Security Access Request"), max_length=400, default = "N/A")
	business_cards = models.CharField(_("Business Cards (if needed provide info to include)"), max_length=100, default = "N/A")
	orientation_date = models.DateField(_("Orientation Date"), default=datetime.date.today)
	_401k_eligible = models.BooleanField(_("401K Eligible"), default = True)
	completed = models.BooleanField(_("Completed"), default = True)
	termination_date = models.DateField(_("Termination Date"), default=datetime.date.today)
	rehire = models.BooleanField(_("Rehire (T/F)"), default = True)

"""
#GENERATE FORM USING MODEL
class PersonForm(ModelForm):
	class Meta:
		model = Person
		#fields = ['person_lastname', 'person_firstname', 'person_title', 'person_date']

"""




















