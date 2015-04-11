from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from s3 import get as s3_get
from s3 import post as s3_post

class Post(models.Model):
  user = models.ForeignKey(User)
  content = models.CharField(max_length = 200)
  image_path = models.CharField(max_length = 200)
  pub_date = models.DateTimeField('date published')
  def __unicode__(self):
    return self.content
  def save(self, *args):
    if not self.pub_date:
      self.pub_date = timezone.now()
    return super(Post, self).save(*args)
  def get_image_url(self):
    return s3_get(self.image_path)

class Comment(models.Model):
  user = models.ForeignKey(User)
  post = models.ForeignKey(Post)
  content = models.CharField(max_length = 200)
  pub_date = models.DateTimeField('date published')
  def save(self, *args):
    if not self.pub_date:
      self.pub_date = timezone.now()
    return super(Comment, self).save(*args)
  def __unicode__(self):
    return self.content






# Create your models here.
