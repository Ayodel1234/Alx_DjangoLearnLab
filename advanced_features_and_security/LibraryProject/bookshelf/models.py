from django.db import models
from django.conf import settings
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.shortcuts import render
from django.contrib.auth.decorators import permission_required


@permission_required("bookshelf.can_view", raise_exception=True)
def view_resource(request):
    return render(request, "view.html")


@permission_required("bookshelf.can_create", raise_exception=True)
def create_resource(request):
    return render(request, "create.html")


@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_resource(request):
    return render(request, "edit.html")


@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_resource(request):
    return render(request, "delete.html")

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username

user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE
)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title


from django.db import models


class Resource(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        permissions = (
            ("can_view", "Can view resource"),
            ("can_create", "Can create resource"),
            ("can_edit", "Can edit resource"),
            ("can_delete", "Can delete resource"),
        )