from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.contrib.auth.models import UserManager as DjangoUserManager
from django.core import validators
from django.db import models
from django.db.models import EmailField
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class BaseModel(TimeStampedModel):
    """Base model for apps' models.

    This class adds to models created and modified fields

    """

    class Meta:
        abstract = True


class UserManager(DjangoUserManager):
    """Adjusted user manager that works w/o `username` field."""

    # pylint: disable=arguments-differ
    def _create_user(self, email, password, **extra_fields):
        """Create and save a user with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # pylint: disable=arguments-differ
    def create_superuser(self, email, password=None, **extra_fields):
        """Create superuser instance (used by `createsuperuser` cmd)."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(
    AbstractBaseUser,
    PermissionsMixin,
    BaseModel,
):
    """Custom user model without username."""

    first_name = models.CharField(
        verbose_name=_("First name"),
        max_length=30,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name=_("Last name"),
        max_length=30,
        blank=True,
    )
    email = EmailField(
        verbose_name=_("Email address"),
        max_length=254,  # to be compliant with RFCs 3696 and 5321
        blank=False,
        unique=True,
        validators=[validators.validate_email],
    )
    is_staff = models.BooleanField(
        verbose_name=_("Staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site.",
        ),
    )
    is_active = models.BooleanField(
        verbose_name=_("Active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active.",
        ),
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    @property
    def full_name(self):
        """Return full name of user."""
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        # pylint: disable=invalid-str-returned
        return self.email
