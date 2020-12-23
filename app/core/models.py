from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from app import settings
# Create your models here.
class UserManager(BaseUserManager):
    #The **extra_fields is a special datatype and it allows us to go past the parameters and still have a reference for them
    def create_user(self, email, password=None, **extra_fields):
        #Create and saves a user
        if not email:
            raise ValueError('Users must have email address')      
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        # creates a superuser
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

#In the Django resources, this is already taught. Im just declaring a user under my specifications
class User(AbstractBaseUser, PermissionsMixin):
    # custom user model that supports creation with email instead of username.
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

class Pizza(models.Model):
    """
    Pizza to be put on the menu
    """
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    ingredients = models.ManyToManyField('Ingredient')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    """
    Ingredients to be put on the pizzAAAAAAAAAAAA
    """
    name = models.CharField(max_length=255)
    #quantity = models.IntegerField(max_length=5)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

class Order(models.Model):
    """
    Orders taken by the waiter
    """
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    pizza = models.ForeignKey(
        'Pizza',
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField()

    # payment = models.ForeignKey(
    #    'Payment',
    #    on_delete=models.CASCADE,
    # )
    is_paid = models.BooleanField(default=False)

class Payment(models.Model):
    """
    Payment for the order
    """
    payment_method = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
