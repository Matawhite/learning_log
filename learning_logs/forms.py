from django import forms
from .models import Topic, Entry

# importing  a lot from the Topic class /learning_logs/models.py

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text': ''}
		widget = {'text': forms.Textarea(attrs={'cols':80})}		

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': ''}
		widget = {'text': forms.Textarea(attrs={'cols':80})}		