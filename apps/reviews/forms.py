from django import forms
from .models import Review

from django import forms
from .models import Review


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'title', 'content', 'advantages', 'disadvantages']

        widgets = {
            'rating': forms.Select(attrs={
                'class': 'form-select',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Коротко про товар'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Ваші враження...'
            }),
            'advantages': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Що вам сподобалось?'
            }),
            'disadvantages': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Що не сподобалось?'
            }),
        }

        labels = {
            'rating': 'Оцінка',
            'title': 'Тема',
            'content': 'Коментар',
            'advantages': 'Переваги',
            'disadvantages': 'Недоліки',
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise forms.ValidationError('Title must contain at least 2 characters.')
        if title.isdigit():
            raise forms.ValidationError('Title cannot consist only of digits.')
        return title.strip()

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError('Review must contain at least 10 characters.')
        if content.lower().count('http') > 3:
            raise forms.ValidationError('Review contains too many links (spam protection).')
        return content.strip()

    def clean_advantages(self):
        advantages = self.cleaned_data.get('advantages')
        return advantages.strip() if advantages else ""

    def clean_disadvantages(self):
        disadvantages = self.cleaned_data.get('disadvantages')
        return disadvantages.strip() if disadvantages else ""