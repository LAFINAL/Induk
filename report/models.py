from django.db import models
from django.conf import settings
from model_rename import RenameFile


class Board(models.Model):
	company = models.CharField(max_length=20, help_text='url에서 쓰이는 이름', unique=True)
	title = models.CharField(max_length=20, help_text='화면에 보여지는 이름', unique=True)
	order = models.PositiveIntegerField(help_text='화면에 표시되는 순서')
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = '기업 리스트'
		verbose_name_plural = '기업 리스트'


class Report(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	board = models.ForeignKey(Board, related_name='board_set')
	title = models.CharField(max_length=30)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	files = models.FileField(null=True, blank=True, upload_to=RenameFile('report/%Y%m%d/'))
	image = models.ImageField(null=True, blank=True, upload_to=RenameFile('report/%Y%m%d/'))
	show = models.BooleanField(default=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = '기업보고'
		verbose_name_plural = '기업보고'


class ReportComment(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	message = models.TextField()
	report = models.ForeignKey(Report)
	# comment = models.ForeignKey("self", blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.report.title

	class Meta:
		verbose_name = '기업보고 댓글'
		verbose_name_plural = '기업보고 댓글'
