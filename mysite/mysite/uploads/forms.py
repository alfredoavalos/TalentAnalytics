from django import forms

types = [('headcount', 'Head Count'), ('dcp', 'DCP'), \
]

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    tipo = forms.ChoiceField(choices = types,widget=forms.Select(choices = types))

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
    tipo = forms.ChoiceField(choices = types,widget=forms.Select(choices = types))
