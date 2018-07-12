from django import forms

types = [('headcount', 'Head Count'), ('dcp', 'DCP'), ('empleado', 'Empleado'),\
(u'desempeño', u'Desempeño'), ('vacante', 'Vacante'), ('potencial', 'Potencial'),\
('hogan', 'Hogan')
]

periodos = [('enero','Enero'),('febrero','Febrero'),('marzo','Marzo'),('abril','Abril'),\
('mayo','Mayo'),('junio','Junio'),('julio','Julio'),('agosto','Agosto'),('setiembre', 'Setiembre'),\
('octubre','Octubre'),('noviembre','Noviembre'),('diciembre','Diciembre')]

class UploadFileForm(forms.Form):
    tipo = forms.ChoiceField(choices = types,widget=forms.Select(choices = types))
    periodo = forms.ChoiceField(choices = periodos, widget=forms.Select(choices=types))
    archivo = forms.FileField()

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
    tipo = forms.ChoiceField(choices = types,widget=forms.Select(choices = types))
