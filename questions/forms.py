from django import forms
from .models import Questions, QuestionsComment


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ('title', 'content', 'files', 'image')


class QuestionsCommentForm(forms.ModelForm):
	class Meta:
		model = QuestionsComment
		fields = ('message',)
