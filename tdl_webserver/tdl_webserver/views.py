from django.views.generic.base import TemplateView
from datetime import datetime

class Intro(TemplateView):
    template_name = 'intro.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'time':datetime.now()
        })
        return context