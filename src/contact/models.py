from django.db import models


class Contact(models.Model):
	A = "A"
	T = "T"
	L = "L"
	O = "O"
	credential_choices = ( (A, "Athlete"),(T, "Team"),(L, "League Organizer"),(O,"Other"),)
	name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Name")
	credential = models.CharField(max_length=200, choices=credential_choices, null=True,blank=True, verbose_name="Credential")
	email = models.CharField(max_length=200, null=True, blank=True, verbose_name='Email Address')
	message = models.TextField(verbose_name="Message", blank=True, null=True)
	beta_registration = models.BooleanField(default=False, verbose_name="Beta Registration")
	datesent = models.DateTimeField(auto_now_add=True, verbose_name="Date")

	def __str__(self):
		return self.name

	# Create your models here.
