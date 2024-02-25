from .admin_site import agence_site
from django.contrib import admin
from agence import models




agence_site.register(models.post)