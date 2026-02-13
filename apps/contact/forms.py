from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Основной класс Bootstrap для инпутов
            'placeholder': 'Enter your name',
        }),
        error_messages={  # Важно: аргумент называется error_messages (во множественном числе)
            'required': "Enter your name",
            'max_length': "Name can't be longer than 100 symbols",
        }
    )

    email = forms.EmailField(
        label='Email',
        validators=[EmailValidator(message='Enter valid email')],
        widget=forms.EmailInput(attrs={  # Важно: Виджет называется EmailInput, а не EmailField
            'class': 'form-control',
            'placeholder': 'your.email@example.com'
        }),
        error_messages={
            'required': "Enter your email",
            'invalid': "Invalid email",
        }
    )

    subject = forms.CharField(
        max_length=200,
        label='Subject',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Subject',
        }),
        error_messages={
            'required': "Enter your subject",
            'max_length': "Subject can't be longer than 200 symbols",
        }
    )

    message = forms.CharField(  # Используем CharField для текста
        max_length=1000,
        label='Message',
        widget=forms.Textarea(attrs={  # Виджет Textarea для большого текста
            'class': 'form-control',
            'placeholder': 'Describe your message',
            'rows': 5,  # Высота поля в строках
        }),
        error_messages={
            'required': "Enter your message",
            'max_length': "Message can't be longer than 1000 symbols",
        }
    )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise forms.ValidationError(
                'Ім\'я повинно містити щонайменше 2 символи.'
            )
        if name.isdigit():
            raise forms.ValidationError(
                'Ім\'я не може складатися лише з цифр.'
            )
        return name.strip()

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 10:
            raise forms.ValidationError(
                'Повідомлення повинно містити щонайменше 10 символів.'
            )
        if message.lower().count('http') > 3:
            raise forms.ValidationError(
                'Повідомлення містить занадто багато посилань.'
            )
        return message.strip()

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        return subject.strip()