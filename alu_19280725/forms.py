from django import forms

STATUS_OP = [
    ("1", "Activo"),
    ("0", "Baja"),
]

class StyledTextInput(forms.TextInput):
    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {'class': 'form-control', 'style': 'width: 800px; padding: 10px;','placeholder': 'Escriba su mensaje...'}
        super().__init__(*args, **kwargs)

class CrearMensaje(forms.Form):
    # contenido = forms.CharField(widget=StyledTextInput)
    contenido = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'mensaje',
            'class': 'form-control',
            'placeholder': 'Escriba su mensaje...',
            'style': 'width: 75%; ',
        }), label=False
    )