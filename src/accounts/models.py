from django.db import models
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.crypto import get_random_string
from send_email.views import SendEmail

#from django.contrib.postgres.fields import JSONField

# Create your models here.
class UserManager(BaseUserManager):
	def create_user(self, email, password, **kwargs):
		user = self.model(
			email=self.normalize_email(email),
			is_active=False,
			**kwargs
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password, **kwargs):
		user = self.model(
			email=email,
			is_staff=True,
			is_superuser=True,
			is_active=True,
			**kwargs
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

class EmailLoginField(models.EmailField):
	def get_prep_value(self, value):
		if value == '':
			return None
		return value

class User(AbstractBaseUser, PermissionsMixin):
	A = "A"
	T = "T"
	L = "L"
	R = "R"
	ADMIN = "Admin"
	credential_choices = ( (A, "Athlete"),
		(T, "Team"),
		(R,"Referee"),
		(L, "League Organizer"),
		(ADMIN, "ADMIN") )

	email = EmailLoginField(unique=True, blank=True, null=True, verbose_name='email address')
	username = models.CharField(max_length=200, unique=True, blank=True, null=True, verbose_name='Username')
	first_name = models.CharField(max_length=200, null=True, blank=True, verbose_name="First Name")
	last_name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Last Name")
	joined = models.DateTimeField(auto_now_add=True)
	date_of_birth = models.DateField(null=True, blank=True, verbose_name="Date of Birth")
	is_active = models.BooleanField(default=False, verbose_name="is active?") # users must confirm email in order to become active
	is_admin = models.BooleanField(default=False, verbose_name="is admin?")
	is_staff = models.BooleanField(default=False, verbose_name="is staff?")
	credential = models.CharField(max_length=200, choices=credential_choices, null=True,blank=True, verbose_name="Credential")
	created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	updated_at = models.DateTimeField(auto_now=True)
	#region = JSONField(default=dict, blank=True, null=True, verbose_name="Region", help_text="json field containining city, state, country")
	objects = UserManager()

	USERNAME_FIELD = 'email'
	#REQUIRED_FIELDS = ['first_name']

	def __str__(self):
		return self.email

	def get_username(self):
		if not self.email:
			return "self"
		else:
			return self.email

class EmailConfirmation(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User")
	token = models.CharField(max_length=128, blank=True, null=True, verbose_name="Generated Token")
	has_confirmed = models.BooleanField(default=False, verbose_name="Confirmed ?", help_text="Has the user confirmed his email?")
	created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	def __str__(self):
		return "[New User] " + self.user.email

# =========================================
# ========= PRE POST SAVE SIGNALS =========
# =========================================

def post_save_email_registration_confirmation(sender, instance, **kwargs):
	if kwargs['created']: # this is only applied when new users are added to the User model
		# SENDING EMAIL TO CONFIRM REGISTRATION AND CREATING TOKEN FOR USER TO VERIFY
		email_instace = SendEmail()
		generated_token = get_random_string(length=64)
		EmailConfirmation.objects.create(user=instance, token=generated_token)
		email_instace.send_confirm_registration(instance.email, generated_token)

# post_save.connect(post_save_email_registration_confirmation, sender=User)


