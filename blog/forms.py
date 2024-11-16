from django import forms
from .models import Categoria


class FormularioCrearPost(forms.Form):
    titulo = forms.CharField(max_length=100,
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Título'
                             }))
    contenido = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Contenido'
        }))
    imagen = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
    categorias = forms.ModelMultipleChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}))


class FormularioEditarPost(forms.Form):
    titulo = forms.CharField(max_length=100,
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Título'
                             }))
    contenido = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Contenido'
        }))
    imagen = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
    categorias = forms.ModelMultipleChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        post = kwargs.pop('post')
        super().__init__(*args, **kwargs)
        
        if post:
            self.fields['titulo'].initial = post.titulo
            self.fields['contenido'].initial = post.contenido
            self.fields['imagen'].initial = post.imagen
            self.fields['categorias'].initial = post.categorias.all()
            
class FormularioComentario(forms.Form):
    texto = forms.CharField(max_length=500,
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Contenido...'
                             }))