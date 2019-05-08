from django.conf.urls import url, include
from django.contrib import admin
from books import views
urlpatterns = [
	url(r'^books/', include('books.urls')),
   	url(r'^admin/', admin.site.urls),
   	url('accounts/', include('django.contrib.auth.urls')),
   	url(r'^logout/$', views.user_logout, name='logout'),
]
