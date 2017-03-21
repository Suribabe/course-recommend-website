from django.db import models

from django.contrib.auth.models import User

class User_profile(models.Model):
	gender = models.CharField(max_length=20, blank=True, default="")
	birthday = models.DateField(blank=True)
	address = models.CharField(max_length=255, blank=True, default="")
	post_number = models.CharField(max_length=10, blank=True, default="")
	phone = models.CharField(max_length=18, blank=True, default="")
	follower = models.ManyToManyField('self', related_name='user_profile')

	def __str__(self):
		return self.text

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=42)
	date = models.DateTimeField('data published')
	text = models.CharField(max_length=300, blank=True, default="")
	location = models.CharField(max_length=255, blank=True, default="")
	category = models.CharField(max_length=10)
	video = models.FileField(upload_to="videos",blank=True)
	like = models.IntegerField()
	dislike = models.IntegerField()

	def __str__(self):
		return self.text

class Image(models.Model):
	owner = models.ForeignKey(Post)
	picture = models.ImageField(upload_to="photos")

	def __str__(self):
		return self.text

class Comment(models.Model):
	owner = models.ForeignKey(Post)
	text = models.CharField(max_length=100)
	date = models.DateTimeField('data published')
	user = models.ForeignKey(User)

	def __str__(self):
		return self.text

class Reply(models.Model):
	comment = models.ForeignKey(Comment)
	text = models.CharField(max_length=100)
	date = models.DateTimeField('data published')
	user = models.ForeignKey(User)

	def __str__(self):
		return self.text

class Recommendation(models.Model):
	user = models.ForeignKey(User)
	userList = models.ForeignKey(User, related_name='user')
	postList = models.ForeignKey(Post, related_name='post')
	update_time = models.DateField()





