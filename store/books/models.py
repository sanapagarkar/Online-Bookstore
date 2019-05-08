from django.db import models

class Section(models.Model):
	genre=models.CharField(max_length=100)
	#genre_id=pk

	def __str__(self):
		return self.genre

class Book(models.Model):
	genre=models.ForeignKey(Section, on_delete=models.CASCADE)
	name=models.CharField(max_length=500)
	author=models.CharField(max_length=30)
	cover=models.CharField(max_length=1000, default="Image not available.")
	about=models.CharField(max_length=10000, default="Description not available.")
	price=models.CharField(max_length=10, default="Book not available for purchase.")
	issueDate=models.CharField(max_length=20, default="Not issued yet.")
	dueDate=models.CharField(max_length=20, default="Not issued yet.")

	def __str__(self):
		return self.name +' - '+ self.author