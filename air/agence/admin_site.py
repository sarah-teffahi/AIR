from django.contrib import admin

class AgenceAdminArea(admin.AdminSite):
    site_header = 'Agence Admin area'

agence_site = AgenceAdminArea(name='agenceadmin')