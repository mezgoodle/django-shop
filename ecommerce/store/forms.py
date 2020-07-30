from django.forms import Form, CharField, EmailField, TextInput, EmailInput, Textarea

class EmailProductForm(Form):
    name = CharField(max_length=25,
                     widget=TextInput(attrs={
                         'class': 'form-control',
                         'placeholder': 'Enter name',
                     }))
    email = EmailField(widget=EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email',
    }))
    to = EmailField(widget=EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter email',
    }))
    comments = CharField(required=False, widget=Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Your comments',
    }))