from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core.validators import RegexValidator


USERNAME_REGEX = '^[a-zA-Z0-9.#]*$'


class UserProfileManager(BaseUserManager):
    """Manager for user profile"""

    def create_user(self, email, username, password=None):
        """Create a new user profile """
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        """Create and save new superuser with given name and details"""
        user = self.create_user(email, username, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the systems """

    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255,
                                unique=True,
                                validators=[
                                    RegexValidator(
                                        regex=USERNAME_REGEX,
                                        message='Username must be AlphaNumeric or contain any of the following regex: [.@#]*$]',
                                        code='invalid_username'
                                    )
                                ],
                                )
                                
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        """Retrieve full name of user """
        return self.username

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.username

    def __str__(self):
        """Return string representation of our user"""
        return self.username