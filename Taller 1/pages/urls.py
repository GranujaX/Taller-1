from django.urls import path
from .views import HomePageView, AboutPageView, ProductIndexView, ProductShowView, ProductCreateView, ContactPageView, done

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path("contact/", ContactPageView.as_view(), name='contact'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('done', done, name='done'), 
]
