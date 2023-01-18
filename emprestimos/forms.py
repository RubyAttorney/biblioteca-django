from django import forms
from .models import Livros, Emprestimo
class LivrosForm(forms.ModelForm):
    class Meta:
        model = Livros
        fields = ['titulo','descricao','quantidade','editora']
        
class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = [ 'livro']
    
    