from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#def home (request):
#	return HttpResponse("Hello, welcome to my app!")

def home(request):
	return render(request, 'home.html')
	
def movies (request):
	return render(request, 'movies.html')
	
def tvshows (request):
	return render(request, 'tvshows.html')
	
def videogames (request):
	return render(request, 'videogames.html')	