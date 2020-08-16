from django.conf import settings
from django.db import models
from embed_video.fields import EmbedVideoField

class Subjects(models.Model):
    name = models.CharField(primary_key=True, max_length=30)

    def __str__(self):
        return self.name

class Ebooks(models.Model):
    subject = models.ForeignKey(Subjects, on_delete=models.SET_NULL, null=True, blank=True)
    ebook_name = models.CharField(max_length=50, null=True, blank=True)
    ebook = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.ebook_name

class Topics(models.Model):
    subject = models.ForeignKey(Subjects, on_delete=models.SET_NULL, null=True, blank=True)
    topic_name = models.CharField(primary_key=True, max_length=50, default='none')
    details = models.TextField(null=True, blank=True)
    i_frame = EmbedVideoField(null=True, blank=True)

    def __str__(self):
        return self.topic_name


class Certificate(models.Model):
    issue_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    certificate_name = models.CharField(max_length=50, null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=True)
    issue_date = models.DateField(auto_now_add=True)
    credentials = models.CharField(primary_key=True, max_length=20)