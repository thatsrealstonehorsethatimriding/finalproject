from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),  # Anasayfa olarak register sayfasını göster
    # Diğer URL'ler buraya eklenebilir
]
