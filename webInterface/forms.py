from django import forms

class ImageForm(forms.Form):
    """ Form field to take video as input """
    image = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-outline-info'}))