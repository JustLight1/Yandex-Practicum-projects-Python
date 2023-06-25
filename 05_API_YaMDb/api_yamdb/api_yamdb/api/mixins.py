from rest_framework import filters, mixins, viewsets

from .permissions import IsAdminOrReadOnly


class MixinsViews(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    """Базовый вьюсет для Category и Genre"""
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
