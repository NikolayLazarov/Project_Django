from django.urls import path
from first_app.views import home, movies, tvshows,videogames
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path ('', home),
	path('movies/', movies),
	path('tvshows/', tvshows),
	path('videogames/', videogames)
	
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)