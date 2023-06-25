from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group."""

    class Meta:
        fields = '__all__'
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        read_only_fields = ('post',)
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Follow."""

    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(slug_field='username',
                                             queryset=User.objects.all())

    def validate_following(self, following):
        """Валидатор запрета подписки на самого себя."""

        if self.context['request'].user == following:
            raise serializers.ValidationError(
                'На себя подписаться нельзя.')
        return following

    class Meta:
        fields = '__all__'
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]
