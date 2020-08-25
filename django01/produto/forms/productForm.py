
from django import forms
from django.core.validators import RegexValidator

from categoria.models import Category
from produto.models import Product
from projeto import settings




class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'category', 'branch', 'price', 'quantity', 'image',  'available')
        localized_fields = ('price',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].error_messages={'required': 'Campo obrigatório.',
                                            'unique': 'Nome de produto duplicado.'}
        self.fields['name'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['category'].error_messages={'required': 'Campo obrigatório'}
        self.fields['category'].queryset=Category.objects.all().order_by('name')
        self.fields['category'].empty_label='--- Selecione uma categoria ---'
        self.fields['category'].widget.attrs.update({'class': 'form-control form-control-sm'})


        self.fields['price'].min_value=0
        self.fields['price'].error_messages={'required': 'Campo obrigatório.',
                                             'invalid': 'Valor inválido.',
                                             'max_digits': 'Mais de 5 dígitos no total.',
                                             'max_decimal_places': 'Mais de 2 dígitos decimais.',
                                             'max_whole_digits': 'Mais de 3 dígitos inteiros.'}
        self.fields['price'].widget.attrs.update({
            'class': 'form-control form-control-sm',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'
        })

        self.fields['quantity'].min_value=0
        self.fields['quantity'].error_messages={
            'required': 'Campo obrigatório',
            'min_value': 'A quantidade deve ser maior ou igual a zero.'
        }
        self.fields['quantity'].widget=forms.TextInput(attrs={
            'class': 'form-control form-control-sm',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'
        })

        self.fields['image'].error_messages={'required': 'Campo obrigatório'}
        self.fields['image'].validators=[
            RegexValidator(regex='^[a-z]+\.(jpg|png|gif|bmp)$', message='Nome de imagem inválido.')]
        self.fields['image'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['image'].required = True

