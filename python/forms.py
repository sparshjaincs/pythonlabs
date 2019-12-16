from django import forms
from .models import forum

class discussion_forum(forms.ModelForm):
	class Meta:
		model = forum
		fields=['email','title','post_text']