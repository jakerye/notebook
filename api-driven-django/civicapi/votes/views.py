from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import (
    BrowsableAPIRenderer, 
    JSONRenderer, 
    TemplateHTMLRenderer
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from votes.models import Vote
from votes.serializers import VoteSerializer


class VoteList(generics.ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    renderer_classes = (
        JSONRenderer,
        TemplateHTMLRenderer, 
        BrowsableAPIRenderer,
    )
    template_name = "vote_list.html"
    permission_classes = (IsAuthenticatedOrReadOnly,)


class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    renderer_classes = (
        JSONRenderer,
        TemplateHTMLRenderer, 
        BrowsableAPIRenderer,
    )
    template_name = "vote_detail.html"
    permission_classes = (IsAuthenticatedOrReadOnly,)
