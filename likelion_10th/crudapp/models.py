from django.db import models
from django.contrib.auth.models import User # 추가

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()
    users = models.ManyToManyField(User, through='Scrap')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Scrap(models.Model):  #추가
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    creared_at = models.DateTimeField(auto_now_add=True)
