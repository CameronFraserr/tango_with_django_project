from django import forms
from rango.models import Page, Category

class CategoryForm(forms.ModelForm):
    # Need to add HiddenInputs for all fields even if we don't input data for them or the form won't return a value for them at all
    name = forms.CharField(max_length=Category.NAME_MAX_LENGTH, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    slug = forms.CharField(widget=forms.HiddenInput, required=False)

    # Inline class that provides additional information on the form
    class Meta:
        model = Category # Provides an association between the ModelForm and a model
        fields = ('name',) # State what fields we want

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=Page.TITLE_MAX_LENGTH, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=Page.URL_MAX_LENGTH, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        exclude = ('category',) # Explicitly states what fields we dont want