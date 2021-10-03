from django import forms

from cities.models import City


# Del class HtmlForm
# class HtmlForm(forms.Form):
#     name = forms.CharField(label='Город')


class CityForm(forms.ModelForm):
    name = forms.CharField(label="Город_label", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите название города',
    }))

    class Meta:
        model = City
        fields = ('name', )
