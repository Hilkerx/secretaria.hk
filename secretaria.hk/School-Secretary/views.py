from django.views.generic.base import TemplateView  # Corrigido o caminho de importação

class Home(TemplateView):
    template_name = "home.html"
