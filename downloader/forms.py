


from django import forms

class DownloadForm(forms.Form):
    url = forms.URLField(label='URL do vídeo', max_length=200)
