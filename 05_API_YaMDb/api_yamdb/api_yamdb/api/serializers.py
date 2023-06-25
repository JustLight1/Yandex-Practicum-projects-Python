from rest_framework import serializers

from api_yamdb.constants import (MAX_LENGTH_USERNAME, MAX_SCORE,
                                 MIN_SCORE, MAX_LENGTH_FIELD_EMAIL)
from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User
from users.validators import validate_username


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User."""

    class Meta:
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )
        model = User


class UserRegistrationSerializer(serializers.Serializer):
    """Сериализатор регистрации User."""

    username = serializers.CharField(
        required=True, max_length=MAX_LENGTH_USERNAME,
        validators=[validate_username])
    email = serializers.EmailField(
        required=True,
        max_length=MAX_LENGTH_FIELD_EMAIL
    )


class TokenSerializer(serializers.Serializer):
    """Сериализатор токена."""

    username = serializers.CharField(
        required=True, max_length=MAX_LENGTH_USERNAME,
        validators=[validate_username],)

    confirmation_code = serializers.CharField(required=True)


class UserEditSerializer(UserSerializer):
    """Сериализатор модели User для get и patch."""

    role = serializers.CharField(read_only=True)


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Category"""

    class Meta:
        model = Category
        exclude = ('id',)


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Genre"""

    class Meta:
        model = Genre
        exclude = ('id',)


class TitleSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Title (предназначенный для чтения данных)."""

    genre = GenreSerializer(many=True)
    category = CategorySerializer()
    rating = serializers.IntegerField(required=False)

    class Meta:
        model = Title
        fields = '__all__'
        read_only_fields = (
            'id', 'name', 'year', 'description', 'genre', 'category', 'rating'
        )


class TitlePostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Title (предназначенный для записи данных)"""

    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(), slug_field='slug', many=True
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field='slug'
    )
    rating = serializers.IntegerField(required=False)

    class Meta:
        model = Title
        exclude = ('id',)
        read_only_fields = ('id', 'rating')

    def to_representation(self, value):
        return TitleSerializer(value, context=self.context).data


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор модели Review"""

    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True,
        default=serializers.CurrentUserDefault()
    )
    score = serializers.IntegerField(
        min_value=MIN_SCORE, max_value=MAX_SCORE
    )

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('title',)

    def validate(self, data):
        if self.context['request'].method == 'POST':
            if Review.objects.filter(
                author=self.context['request'].user,
                title=self.context['view'].kwargs.get('title_id')
            ).exists():
                raise serializers.ValidationError(
                    'Нельзя оставить отзыв на одно произведение дважды'
                )
        return data


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор модели Comment"""

    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review',)
