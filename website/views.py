from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class AboutView(TemplateView):
    template_name = "about.html"


class LoginView(TemplateView):
    template_name = "login.html"
