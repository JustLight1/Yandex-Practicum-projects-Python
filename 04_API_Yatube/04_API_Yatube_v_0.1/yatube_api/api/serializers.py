from rest_framework import serializers

from posts.models import Comment, Group, Post

# Меня подставили) isort почему-то помечает такое расположение как ошибку и
# сортирует неправильно, впредь буду внимательнее. Спасибо <3.


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(),
                                               required=False)

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')
        read_only_fields = ('author',)
        model = Post


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('author', 'post')
        model = Comment
