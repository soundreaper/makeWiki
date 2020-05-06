from django import forms
from wiki.models import Page


class PageCreateForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    model = Page