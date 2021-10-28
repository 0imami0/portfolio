from django.shortcuts import render
from django.http import HttpResponse



def home(request):
	return render(request, 'base/home.html')



def projects(request, pk):
	if pk == 1:
		temp = 'base/crm.html'
	elif pk == 2:
		temp = 'base/charts.html'
	elif pk == 3:
		temp = 'base/bot.html'
	elif pk == 4:
		temp = 'base/gol.html'
	return render(request, temp)
	