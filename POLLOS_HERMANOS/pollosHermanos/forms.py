from django import forms 
from pollosHermanos.models import Reserva
import datetime

class DateInput(forms.DateInput):
    input_type='date'

class TimeInput(forms.TimeInput):
    input_type='time'

def fechaActual():
    """
    Funcion que toma la fecha actual, la transforma en un String
    y la devuelve. Su implementacion esta para limitar la fecha de ingreso 
    para las reservas.
    """
    tiempo=datetime.date.today()
    str(tiempo)
    return (tiempo)

class FormReserva(forms.ModelForm):
    class Meta:
        model=Reserva
        fields=(
            'nombrePersona', 
            'telefono',
            'fechaReserva',
            'horaReserva',
            'cantidadPersonas',
            'estadoReserva',
            'observacion',
            )
        widgets={
            'nombrePersona': forms.TextInput(attrs={'class': 'form-control', 'required':'',}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'required':'',}),
            'fechaReserva': DateInput(attrs={'class': 'form-control', 'required':'', 'min':'%s'%fechaActual(),}),
            'horaReserva': TimeInput(attrs={'class': 'form-control', 'required':'', 'placeholder': '12:34',}),
            'cantidadPersonas': forms.NumberInput(attrs={'class': 'form-control', 'required':'', 'min':'1', 'max':'15'}),
            'estadoReserva': forms.Select(attrs={'class': 'form-control', 'required':'',}),
            'observacion': forms.Textarea(attrs={'class': 'form-control',}), 
        }