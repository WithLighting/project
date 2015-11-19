from django.shortcuts import render
from django.template import *
from django.shortcuts import render_to_response
from mybooks.models import Book,Author
from django.contrib import auth
from django import forms

def welcome(request):
	return render_to_response('localhost.html')
def searchlist(request):
    errors = []
    if 'Author' in request.GET:
        name1 = request.GET['Author']
        if not name1:
            errors.append('Please enter a search term!')
        else:
            auth_name_list = []
            for auth in Author.objects.all():
                auth_name_list.append(auth.Name)
            if name1 in auth_name_list:
                author_id = Author.objects.get(Name=name1).AuthorID
                books = Book.objects.filter(AuthorID=author_id)
                return render_to_response('search_list.html', {'books': books, 'query': name1})
            else:
                errors.append('No author found!')
                return render_to_response('localhost.html',{'errors': errors})
    return render_to_response('localhost.html')
    
def deleter(request):
	if request.GET:
		if "id1" in request.GET:
			Book.objects.get(ISBN=str(request.GET["id1"])).delete()
	books = Book.objects.all()
	return render_to_response("restbook.html",{"books":books}) 
def information(request):
    if request.GET:
        if "id1" in request.GET:
            tempa = Book.objects.get(ISBN=str(request.GET["id1"])).AuthorID
            ibook = Book.objects.get(ISBN=str(request.GET["id1"]))
    return render_to_response("detail.html",{"ibook":ibook,"author":tempa})

    