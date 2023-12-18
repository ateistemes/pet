from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text' : 'Your Comment'}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Customize the form widget attributes if needed
            self.fields['text'].widget.attrs.update({'class': 'form-control', 'rows': 4})