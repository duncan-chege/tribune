from django import forms        #Import forms module from django
from .models import Article

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label="First Name", max_length=30)
    email = forms.EmailField(label="Email")

class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article     #define what model we are defining the form from
        exclude = [ 'editor','pub_date' ]       #exclude attribute to define what fields we do not want to create from the model
        widgets = {         #define widgets from the app
            'tags': forms.CheckboxSelectMultiple()      #checkbox due to manytomany relationship
        }
