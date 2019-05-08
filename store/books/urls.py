from django.conf.urls import url
from . import views

urlpatterns = [
	#books/
	url(r'^$', views.index, name='index'),

	#books/register
	url(r'^register/$', views.UserFormView.as_view(), name='register'),
	
	#books/bookindex.html/
	url(r'^bookindex.html/$', views.bookindex, name='bookindex'),

	url(r'^registration.html/$', views.registration, name='registration'),

	#books/index.html/index.html
	#url(r'^index.html/index.html$', views.index, name='index'),

	#books/123/
	url(r'^(?P<genre_id>[0-9]+)/$', views.detail, name='detail'), 

	#books/123/123/
	url(r'^(?P<genre_id>[0-9]+)/(?P<book_id>[0-9]+)/$', views.bookdetail, name='bookdetail'),

	#bookd/123/123/form.html/
	url(r'^(?P<genre_id>[0-9]+)/(?P<book_id>[0-9]+)/form.html/$', views.form, name='form'),

	url(r'^(?P<genre_id>[0-9]+)/(?P<book_id>[0-9]+)/form.html/rent.html/$', views.rent, name='rent'),

	url(r'^user_logout/$', views.user_logout,name='user_logout'),


]
