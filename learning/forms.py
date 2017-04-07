from django import forms
from .models import Learning, LearningComment


class LearningForm(forms.ModelForm):
	class Meta:
		model = Learning
		fields = ('title', 'content', 'files', 'image')


class LearningCommentForm(forms.ModelForm):
	class Meta:
		model = LearningComment
		fields = ('message',)
