from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('update/<int:id>', views.FileUpdateView.as_view(), name='update_file'),
]