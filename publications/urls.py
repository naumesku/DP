from django.urls import path
from publications.apps import PublicationsConfig
from publications.views import *

app_name = PublicationsConfig.name

urlpatterns = [
    path('', PublicationsListView.as_view(), name='index'),
    path('create/', PublicationCreateView.as_view(), name='create'),
    path('view/<int:pk>/', PublicationsDetailView.as_view(), name='view'),
    path('update/<int:pk>/', PublicationsUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PublicationsDeleteView.as_view(), name='delete'),
    path('my_public/', main_public, name='my_public'),
]
