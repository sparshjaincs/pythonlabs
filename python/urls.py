from django.urls import path
from . import views

urlpatterns=[
	path('',views.homepage,name="homepage"),
	path('index/',views.homepage,name="Index"),
	path('buttons/',views.buttons,name="Buttons"),
	
]