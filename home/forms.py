from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text',
                                                         'class': 'contact__input item-input contact__input-const'}),  #, 'placeholder': 'Ваше имя'
                                    label='', required=False)
    email = forms.CharField(widget=forms.TextInput(attrs={'type': 'text',
                                                          'class': 'contact__input item-input contact__input-const'}),
                                    label='', required=False)
    title = forms.CharField(widget=forms.TextInput(attrs={'type': 'text',
                                                          'class': 'contact__input item-input contact__input-const'}),
                                    label='', required=False)
    message = forms.CharField(widget=forms.Textarea(attrs={'type': 'text', 'cols': '30', 'rows': '7',
                                                           'class': 'contact__input item-input contact__input-const'}),
                                    label='', required=False)

    class Meta:
        model = ContactModel
        fields = '__all__'
