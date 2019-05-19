from django.urls import path

from .views import HomePageView, AboutPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # when using Class based views, always add as_view()
    path('about/', AboutPageView.as_view(), name='about')
]