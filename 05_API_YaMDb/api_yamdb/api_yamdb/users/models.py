from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import validate_username

MAX_LENGTH_FIELD_NAME: int = 150
MAX_LENGTH_FIELD_EMAIL: int = 254
MAX_LENGTH_FIELD_ROLE: int = 64


class User(AbstractUser):
    """Модель User."""

    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'

    ROLE_CHOICES = [
        (ADMIN, 'Администратор'),
        (MODERATOR, 'Модератор'),
        (USER, 'Пользователь'),
    ]

    username = models.CharField(
        'Имя пользователя (никнейм)', validators=[validate_username],

        max_length=MAX_LENGTH_FIELD_NAME, unique=True
    )
    email = models.EmailField(
        'Почта', max_length=MAX_LENGTH_FIELD_EMAIL, unique=True
    )
    role = models.CharField(
        'Роль', max_length=MAX_LENGTH_FIELD_ROLE,
        choices=ROLE_CHOICES, default=USER
    )
    bio = models.TextField('Об авторе', null=True, blank=True)
    first_name = models.CharField(
        'Имя', max_length=MAX_LENGTH_FIELD_NAME, null=True, blank=True)
    last_name = models.CharField(
        'Фамилия', max_length=MAX_LENGTH_FIELD_NAME, null=True, blank=True
    )

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser or self.is_staff

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ('id',)
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.username
