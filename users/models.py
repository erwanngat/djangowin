#from django.db import models
#from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
#
## Create your models here.
#class CustomUserManager(UserManager):
#    def _create_user(self, email, password, account_type, **extra_fields):
#        if not email:
#            raise ValueError('You have not provided an email adress')
#        
#        email = self.normalize_email(email)
#        user = self.model(email=email, **extra_fields)
#        user.set_password(password)
#        user.save(using=self._db)
#
#        return user
#
#class User(AbstractBaseUser, PermissionsMixin): 
#    email = models.EmailField(blank=True, default='', unique=True)
#    name = models.CharField(max_length=255, blank=True, default='')
#    account_type = models.IntegerField(default=1)


# Continuer de suivre le tuto ytb sur auth custom