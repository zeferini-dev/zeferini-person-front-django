from django import forms


class PersonForm(forms.Form):
    """Form for creating and editing persons."""
    
    name = forms.CharField(
        max_length=120,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o nome completo',
            'autocomplete': 'off',
        }),
        error_messages={
            'required': 'O nome é obrigatório',
            'max_length': 'O nome deve ter no máximo 120 caracteres',
        }
    )
    
    email = forms.EmailField(
        max_length=180,
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'exemplo@email.com',
            'autocomplete': 'off',
        }),
        error_messages={
            'required': 'O e-mail é obrigatório',
            'invalid': 'Digite um e-mail válido',
            'max_length': 'O e-mail deve ter no máximo 180 caracteres',
        }
    )
