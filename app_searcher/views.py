from django.shortcuts import render
import play_scraper
from app_store_scraper import AppStore
from itunes_app_scraper.scraper import AppStoreScraper
from pprint import pprint


def home(request):
	return render(request,'home.html')

#google_play_store

def google_app_search_page(request):
	return render(request,'google/google_app_search_page.html')

def google_app_search(request):
	print("hello")
	if request.method == "POST":
		app_name = request.POST['search']
		content = play_scraper.details(app_name,)
		#for key in content.keys():
		#	print(key)
		title = content['title']
		developer = content['developer']
		description = content['description']
		icon = content['icon']
		installs = content['installs']
		score = content['score']
		reviews = content['reviews']
		
		print(title,developer)
		

		return render(request,'google/google_success.html',{'title':title,'developer':developer,'description':description,'icon':icon,'installs':installs,'score':score,'reviews':reviews})
	else:
		return render(request,'google/google_failed.html')


#apple_app_store

def apple_app_search_page(request):
	return render(request,'apple/apple_app_search_page.html')

def apple_app_search(request):
	if request.method == "POST":
		search = request.POST['search']
		app_name = AppStore(country="us", app_name=search)
		app_name.review(how_many=20)
		pprint(app_name.reviews)
		pprint(app_name.reviews_count)
		return render(request,'apple/apple_success.html')
	else:
		return render(request,'apple/apple_failed.html')