from django.views.generic import TemplateView


class HomePageView(TemplateView):  # class names, unlike functions, should always be capitalized
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'
