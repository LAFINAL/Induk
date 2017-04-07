from django.db import models
from django.conf import settings
from model_rename import RenameFile


class Notice(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.CharField(max_length=30)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	files = models.FileField(null=True, blank=True, upload_to=RenameFile('notice/%Y%m%d/'))
	image = models.ImageField(null=True, blank=True, upload_to=RenameFile('notice/%Y%m%d/'))
	show = models.BooleanField(default=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = '공지사항'
		verbose_name_plural = '공지사항'


class NoticeComment(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	message = models.TextField()
	notice = models.ForeignKey(Notice)
	# comment = models.ForeignKey("self", blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.notice.title

	class Meta:
		verbose_name = '공지사항 댓글'
		verbose_name_plural = '공지사항 댓글'
