from django.urls import path, include

from .views import HomePageView, InputFormView, LoginPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('input/', InputFormView.as_view(), name='input')

]