from django.views.generic.base import TemplateView

class RequestTemplateView(TemplateView):
    def get_context_data(self, **kwargs):
