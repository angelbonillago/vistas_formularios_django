from django import forms

# creating a form
class InputForm(forms.Form):

    aula = forms.CharField(max_length = 3)
    hora_entrada = forms.TimeField(
        help_text="Ingrese la hora en formato HH:MM"
        )