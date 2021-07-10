from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [

	path('',views.home,name = 'home'),

	#google_play_store
	path('google_app_search_page',views.google_app_search_page,name="google_app_search_page"),
	path('google_app_search',views.google_app_search,name="google_app_search"),

	#apple_app_store
	path('apple_app_search_page',views.apple_app_search_page,name="apple_app_search_page"),
	path('apple_app_search',views.apple_app_search,name="apple_app_search"),

	]
