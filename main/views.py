from django.shortcuts import render
from django.views.generic import ListView

from main.models import Card


class CardListView(ListView):
    queryset = Card.objects.all()
    template_name = 'index.html'
    context_object_name = 'cards'

