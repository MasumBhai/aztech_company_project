from django import forms
from aztech.models import CommentBox,BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('author','title','slug','content','postImage')
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control z-depth-1',
                                             'rows': '5', 'cols': '6',
                                             'placeholder': 'Write your thoughts here...'}),
            'slug': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'give a dashing link that will be added for your post'}),
            'postImage': forms.FileInput,
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentBox
        fields = ('commentator_name', 'commentator_email', 'comment_body')
        widgets = {
            'comment_body': forms.Textarea(attrs={'class': 'form-control z-depth-1',
                                                  'rows': '4','cols': '6',
                                                  'placeholder': 'Write comments here...'}),
        }

