from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Post(models.Model):
	title = models.CharField(verbose_name='Title',max_length=200, blank=False)
	content = models.TextField(verbose_name='Content',max_length=1000,blank=True)
	date_add = models.DateTimeField(verbose_name='Date created ',editable=False, default=now)
	user_add = models.ForeignKey(User,verbose_name='User')
	image = models.ImageField(verbose_name='Image to post', upload_to= 'pic_post', blank=True)
	active = models.BooleanField('Active post', default=True)

	def __str__(self):
		return self.title