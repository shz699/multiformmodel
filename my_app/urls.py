from django.urls import path
from .views import UpdateExist

app_name = 'my_app'

urlpatterns = [
    path('excli/<int:pk>', UpdateExist , name='excli' ),
]
