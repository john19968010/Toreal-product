from django.db import models
from TOREAL.storage import ImageStorage


class User(models.Model):
	fullname = models.CharField(blank=True ,max_length=20)
	nickname = models.CharField(blank=True, max_length=20)
	gender = models.CharField(blank=True, max_length=10)
	find_gender = models.CharField(blank=True, max_length=10)
	age = models.DateTimeField(blank=True)
	height = models.CharField(blank=True, max_length=10)
	county = models.CharField(blank=True, max_length=10)
	district = models.CharField(blank=True, max_length=10)
	email= models.EmailField(blank=True)
	password = models.CharField(blank=True ,max_length=50)
	image = models.ImageField(upload_to='./static/user_image', storage=ImageStorage())
	interest1 = models.CharField(blank=True ,max_length=10)
	interest2 = models.CharField(blank=True ,max_length=10)
	interest3 = models.CharField(blank=True ,max_length=10)
	interest4 = models.CharField(blank=True ,max_length=10)
	interest5 = models.CharField(blank=True ,max_length=10)
	test = models.CharField(blank=True ,max_length=20)

	def __str__(self):     #最後需新增時間
		return '{}, {}, {}'.format(self.fullname, self.gender, self.age) 


class Card(models.Model):
	card_name = models.CharField(blank=True ,max_length=20)
	card_msg = models.TextField(blank=True)
	card_url = models.CharField(blank=True ,max_length=100)
	def __str__(self):
		return '{}, {}, {}'.format(self.card_name, self.card_msg, self.card_url) 



