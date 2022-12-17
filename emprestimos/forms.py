from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Livros, Emprestimo
class LivrosForm(ModelForm):
    class Meta:
        model = Livros
        fields = ['titulo','descricao','quantidade','editora','autor']

class EmprestimoForm(ModelForm):
    class Meta:
        model = Emprestimo
        fields = [ 'livro']
    
    