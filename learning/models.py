from django.db import models
from django.conf import settings
from model_rename import RenameFile


class Learning(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    files = models.FileField(null=True, blank=True, upload_to=RenameFile('learning/%Y%m%d/'))
    image = models.ImageField(null=True, blank=True, upload_to=RenameFile('learning/%Y%m%d/'))
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '학습자료'
        verbose_name_plural = '학습자료'


class LearningComment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    message = models.TextField()
    learning = models.ForeignKey(Learning)
    # comment = models.ForeignKey("self", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.learning.title

    class Meta:
        verbose_name = '학습자료 댓글'
        verbose_name_plural = '학습자료 댓글'
