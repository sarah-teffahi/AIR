
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from agence import views
from agence.admin import agence_site


urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('', views.home, name='home'),
    path('agencesite/', agence_site.urls),
    # path('', include('agence.urls')),
   
    #path('agenceadmin/', agence_site.urls),

  
   
]

admin.site.index_title='Air Algerie'
admin.site.site_header='Air Algerie admin '
admin.site.site_title='agence'


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
