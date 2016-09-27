# coding=utf-8
import json

from django.views.generic.base import TemplateView
from django.middleware.csrf import get_token


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        # constants definition
        context['cdn'] = 'http://localhost:8889/'
        return context

