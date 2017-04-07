from django import forms
from .models import Report, Board, ReportComment


class ReportForm(forms.ModelForm):
	# board = forms.ModelChoiceField(widget=forms.Select(attrs={'size':'13'}), queryset=Board.objects.all())

	class Meta:
		model = Report
		fields = ('title', 'content', 'files', 'image')

class ReportCommentForm(forms.ModelForm):
	class Meta:
		model = ReportComment
		fields = ('message',)
