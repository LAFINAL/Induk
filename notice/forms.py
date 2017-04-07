from django import forms
from .models import Notice, NoticeComment


class NoticeForm(forms.ModelForm):
	class Meta:
		model = Notice
		fields = ('title', 'content', 'files', 'image')


class NoticeCommentForm(forms.ModelForm):
	class Meta:
		model = NoticeComment
		fields = ('message',)
