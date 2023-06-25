from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import User

from api_yamdb.constants import (MAX_LENGTH_FIELD_NAME, MAX_LENGTH_FIELD_SLUG,
                                 NUM_POSTS_PAGE, MIN_SCORE, MAX_SCORE,
                                 SCORE_DEFAULT)
from .validators import validate_year


class Category(models.Model):
    """Модель категории"""
    name = models.CharField(
        max_length=MAX_LENGTH_FIELD_NAME,
        verbose_name='Название',
        help_text='Дайте название категории',
    )
    slug = models.SlugField(
        max_length=MAX_LENGTH_FIELD_SLUG,
        unique=True,
        verbose_name='Адрес для страницы категории',
        help_text=(
            'Укажите адрес для страницы категории. '
            'Используйте только латиницу, цифры, '
            'дефисы и знаки подчёркивания'
        ),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class Genre(models.Model):
    """Модель жанр"""
    name = models.CharField(
        max_length=MAX_LENGTH_FIELD_NAME,
        verbose_name='Название',
        help_text='Дайте название жанра',
    )
    slug = models.SlugField(
        max_length=MAX_LENGTH_FIELD_SLUG,
        unique=True,
        verbose_name='Адрес для страницы жанра',
        help_text=(
            'Укажите адрес для страницы жанра. '
            'Используйте только латиницу, цифры, '
            'дефисы и знаки подчёркивания'
        ),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('name',)


class Title(models.Model):
    """Модель произведения."""
    name = models.CharField('Название', max_length=MAX_LENGTH_FIELD_NAME)
    year = models.PositiveSmallIntegerField(
        'Год', validators=[validate_year], db_index=True)
    description = models.TextField('Описание', null=True, blank=True)
    genre = models.ManyToManyField(Genre, through='GenreTitle')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='category',
        verbose_name='категория'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'произведение'
        verbose_name_plural = 'произведения'

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    """Модель связи произведения с жанром."""
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE, verbose_name='жанры')

    def __str__(self):
        return f'{self.title} {self.genre}'

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'


class BaseReviewCommentModel(models.Model):
    """Базовый абстрактный класс для Review и Comment."""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ('-pub_date',)

    def __str__(self) -> str:
        return self.text[:NUM_POSTS_PAGE]


class Review(BaseReviewCommentModel):
    """Модель отзывы на произведения."""
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, verbose_name='Произведение'
    )
    score = models.PositiveSmallIntegerField(
        'Оценка', default=SCORE_DEFAULT,
        validators=[
            MinValueValidator(MIN_SCORE, f'Минимальная оценка {MIN_SCORE}'),
            MaxValueValidator(MAX_SCORE, f'Максимальная оценка {MAX_SCORE}')
        ]
    )

    class Meta(BaseReviewCommentModel.Meta):
        ordering = ('-pub_date',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        default_related_name = 'reviews'
        constraints = [
            models.UniqueConstraint(
                fields=('author', 'title'),
                name='unique_review'
            )
        ]


class Comment(BaseReviewCommentModel):
    """Модель комментарии к отзывам."""
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, verbose_name='Отзыв'
    )

    class Meta(BaseReviewCommentModel.Meta):
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        default_related_name = 'comments'
        ordering = ('-pub_date',)
