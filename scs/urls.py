from django.urls import path, include
from sklep.views import lista_produktow  # Upewnij się, że ścieżka importu jest poprawna
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produkty/', lista_produktow, name='lista_produktow'),
    # Możesz także użyć include jeśli 'sklep' ma własny urls.py
    # path('sklep/', include('sklep.urls')),
]
