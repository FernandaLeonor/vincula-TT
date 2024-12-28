from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import pgettext_lazy


class UserManagerCustom(UserManager):
    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(
                pgettext_lazy(
                    "User manager Exception",
                    "First you need to provide an email for continue",
                )
            )

        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        if password:
            user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.EmailField(
        unique=True,
        verbose_name=pgettext_lazy("User model field", "email"),
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManagerCustom()

    class Meta:
        db_table = "user"
        managed = True
        verbose_name = pgettext_lazy("User model meta", "User")
        verbose_name_plural = pgettext_lazy("User model meta", "Users")
        ordering = ["id"]

    def __str__(self):
        return f"{self.username} - {self.email}"

    def deactivate(self):
        self.is_active = False
        self.save()

    def reactivate(self):
        self.is_active = True
        self.save()
