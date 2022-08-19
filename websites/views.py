from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
		'form':form,
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
	""" 
		Function for updating an alreay existing page 
		arg:
			pk: Special address for editing the template from the page
	"""
	control = Website.objects.get(pk=pk)
	if request.method == "POST":
		title = request.POST['title']
		html = request.POST['html']
		css = request.POST['css']
		author = request.user
		control.title = title
		control.html = html
		control.css = css
		control.author = author
		control.save()
	return JsonResponse({'result':serialize('json', [control])})

@login_required(login_url="accounts:login")
def view_webpage(request, pk):
	""" 
		Function for viewing websites created 
		arg:
			pk: Special address to the website to visit
	"""
	card = Website.objects.get(pk=pk)
	return render(request, 'website/show.html', {'card':card})

@login_required(login_url="accounts:login")
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
		return redirect('cmsapp:error')
	context = {
		'baltimore':baltimore,
		'tab':tabluex,
		'mon':monkey,
	}
	return render(request, 'website/create.html', context)

@login_required(login_url="accounts:login")
def edit_webpage(request, pk):
	""" 
		Function used to edit the already saved template
		args:
			pk: Special argument used to delete the website
	"""
	card = Website.objects.get(pk=pk)
	return render(request, 'website/edit.html', {'card':card})
