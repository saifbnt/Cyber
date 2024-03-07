# monapp/urls.py
from django.urls import path
from .views import scan_site
from .views import sqlmap_test  # Assurez-vous que l'importation est correcte


urlpatterns = [
    path('scan/', scan_site, name='scan_site'),
    path('api/sqlmap_test/', sqlmap_test, name='sqlmap_test'),



]

