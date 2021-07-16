from django import forms
from aztech.models import CommentBox


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentBox
        fields = ('commentator_name', 'commentator_email', 'comment_body')

