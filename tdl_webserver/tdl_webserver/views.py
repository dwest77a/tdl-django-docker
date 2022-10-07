from django.views.generic.base import TemplateView

class Intro(TemplateView):
    template_name = 'intro.html'
    print('Intro page built successfully')
