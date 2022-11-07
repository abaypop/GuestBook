from django.urls import path
from .views import index

urlpatterns = [    
  # path('', BukuTamuView ),
  path('', index, name="index"),
]