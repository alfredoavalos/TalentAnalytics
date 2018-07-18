from django import forms
from datetime import datetime, timedelta

#('headcount', 'Head Count'),
types = [('empleado', 'Empleados'),(u'desempeño', u'Desempeño'), ('vacante', 'Vacante'),\
 ('potencial', 'Potencial'),('hogan', 'Hogan')]

months = {
    1: 'Enero',\
    2: 'Febrero',\
    3: 'Marzo',\
    4: 'Abril',\
    5: 'Mayo',\
    6: 'Junio',\
    7: 'Julio',\
    8: 'Agosto',\
    9: 'Setiembre',\
    10: 'Octubre',\
    11: 'Noviembre',\
    12: 'Diciembre',\
}
years = [(datetime.today()+timedelta(days=30 * i)).year for i in range(1,13)]
month = [months[(datetime.today()+timedelta(days=30 * i)).month] for i in range(1,13)]
periodos = [(month[i].lower(), month[i]+' '+str(years[i])) for i in range(11)]

class UploadFileForm(forms.Form):
    tipo = forms.ChoiceField(choices = types,widget=forms.Select(choices = types))
    periodo = forms.ChoiceField(choices = periodos, widget=forms.Select(choices=types))
    archivo = forms.FileField()
