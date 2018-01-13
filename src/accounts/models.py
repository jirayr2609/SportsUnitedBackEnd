from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

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
	email = EmailLoginField(unique=True, blank=True, null=True, verbose_name='email address')
	first_name = models.CharField(max_length=200, null=True, blank=True, verbose_name="First Name")
	last_name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Last Name")
	joined = models.DateTimeField(auto_now_add=True)
	date_of_birth = models.DateField(null=True, blank=True, verbose_name="Date of Birth")
	is_active = models.BooleanField(default=True, verbose_name="is active?")
	is_admin = models.BooleanField(default=False, verbose_name="is admin?")
	is_staff = models.BooleanField(default=False, verbose_name="is staff?")
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



