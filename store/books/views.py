from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
#from django.template import loader
from .models import Section, Book
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from django.urls import reverse 
from django.contrib.auth.decorators import login_required


def index(request):
	all_Sections=Section.objects.all()
	#template=loader.get_template('books/index.html') --needed for HttpResponse
	context={'all_Sections' : all_Sections}
	return render(request,'books/index.html', context)

def detail(request, genre_id):
	#return HttpResponse("Section : "+str(genre_id))
	try:
		genre= Section.objects.get(id=genre_id)
		#all_books=Book.objects.get(genre=genre)
		context={
			#'all_books' : all_books,
			'genre' : genre
		}
	except SectionDoesNotExist:
		raise Http404("Section does not exist")
	return render(request, 'books/detail.html', context)

def bookdetail(request,genre_id, book_id):
	try:
		book= Book.objects.get(id=book_id)
	except BookNotFound:
		raise Http404("Book not found")
	return render(request, 'books/bookdetail.html', {'book' : book})

def form(request, genre_id, book_id):
	return render(request, 'books/form.html',{'book_id':book_id, 'genre_id':genre_id})

def bookindex(request):
	all_books=Book.objects.all()
	#template=loader.get_template('books/index.html') --needed for HttpResponse
	context={'all_books' : all_books}
	return render(request,'books/bookindex.html', context)

def rent(request,genre_id,book_id):
	return render(request,'books/rent.html', {'book_id': book_id})

def registration(request):
	return render(request, 'books/registration.html')


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))


class UserFormView(View):
	form_class = UserForm
	template_name = 'books/registration.html'

	#display a blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form' : form})

	#process from data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			#cleaned/normalized data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()


			#returns User objects if credentials are correct
			user = authenticate(username='username', password='password')

			if user is not None:

				if user.is_active:
					login(request, user)
					return HttpResponseRedirect(reverse(index))
				else:
					return HttpResponse("User not active.")
		return render(request, self.template_name, {'form' : form})

