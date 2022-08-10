from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .pagination import PaginatorWithPagesCount
from .serializers import RelativeSerializer
from .models import Relative

class RelativeViewSet(viewsets.ModelViewSet):
    serializer_class = RelativeSerializer
    permission_classes = [IsAuthenticated]
    queryset = Relative.objects.all()
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = ('name')
    ordering_fields = ('birthdate')
    pagination_class = PaginatorWithPagesCount

class ParentViewSet(RelativeViewSet):
    """
    List all member's parents
    """
    def get_queryset(self):
        parents_query_dict = self.get_parents_query_dict()
        if parents_query_dict:
            try:
                id = parents_query_dict['id']
                member = Relative.objects.filter(id=id)
                parents_ids = member.values_list('parents__id')
                return Relative.objects.filter(id__in=parents_ids)
            except ValueError:
                raise Http404
        else:
            return self.queryset

class SiblingViewSet(RelativeViewSet):
    """
    List all member's siblings
    """
    def get_queryset(self):
        parents_query_dict = self.get_parents_query_dict()
        if parents_query_dict:
            try:
                id = parents_query_dict['id']
                member = Relative.objects.filter(id=id)
                parents_ids = member.values_list('parents__id')
                # Exclude current member
                queryset = Relative.objects.filter(
                            parents__in=parents_ids).exclude(id=id)
                return queryset
            except ValueError:
                raise Http404
        else:
            return self.queryset
