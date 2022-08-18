from django.shortcuts import render
from django.contrib.auth.decorators import Login_required
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Website
from .forms import WebsiteForm
from django.contrib import messages
import json
# Create your views here.

def list_all_websites(request):
	""" Function to list all websites """
	form = Website.objects.filter(author=request.user)
	context = {
		'form':form
	}
	return render(request, 'website/list.html', context)

def savepage(request):
	""" Function for creating a page and sending a json request """
	if request.method == "POST":
		title = request.POST['title']
		html = request.POST['html']
		css = request.POST['css']
		author = request.user
		control = Website.objects.create(
			title=title,
			html=html,
			css=css,
			author=author
		)
		control.save()
	return JsonResponse({'result': serialize('json', [control])})

def editpage(request, pk):
	""" Function for updating an alreay existing page """
	if request.method == "POST":
		title = request.POST['title']
		html = request.POST['html']
		css = request.POST['css']
		author = request.user
		control = Website.objects.get(pk=pk)
		control.title = title
		control.html = html
		control.css = css
		control.author = author
		control.save()
	return JsonResponse({'result':serialize('json', [control])})

def view_webpage(request, pk):
	""" Function for viewing websites created """
	card = Website.objects.get(pk=pk)
