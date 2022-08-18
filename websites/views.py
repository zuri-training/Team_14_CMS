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
	baltimore = {}
	context = {
		'form':form,
		'baltimore':baltimore,
	}
	for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']:
		baltimore[f'template__{i}'] = f"template__{i}"
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
	""" 
		Function for updating an alreay existing page 
		arg:
			pk: Special address for editing the template from the page
	"""
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
	""" 
		Function for viewing websites created 
		arg:
			pk: Special address to the website to visit
	"""
	card = Website.objects.get(pk=pk)
	return render(request, 'website/show.html', {'card':card})

def create_webpage(request, monkey):
	""" 
		Function used for rendering the page for creating the webpage from existing template
		arg:
			monkey: Argument ment to help select the template to be used
	"""
	baltimore = {}
	for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']:
		baltimore[f'template__{i}'] = i
	try:
		tabluex = baltimore[monkey]
	except Exception as e:
		return render(request, '404.html')
	return render(request, 'website/create.html')

def edit_webpage(request, pk):
	""" 
		Function used to edit the already saved template
		args:
			pk: Special argument used to delete the website
	"""
	card = Website.object.get(pk=pk)
	return render(request, 'website/edit.html', {'card':card})
