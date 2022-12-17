from django.db import models
import uuid
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.
class Editora(models.Model):
    nome = models.CharField("Nome", max_length=50)

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField("Nome", max_length=50)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name="Autor"
        verbose_name_plural="Autores"

class Livros(models.Model):
    titulo = models.CharField("Titulo", max_length=200)
    descricao = models.TextField("Descrição")
    data = models.DateField(auto_now_add=True)
    quantidade = models.PositiveIntegerField("Quantidade")
    editora = models.ForeignKey(Editora, on_delete=models.DO_NOTHING)
    autor = models.ForeignKey(Autor, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name="Livro"
        verbose_name_plural="Livros"

class Emprestimo(models.Model):
    codigo = models.UUIDField(default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    data_emp = models.DateField(auto_now_add=True)
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING, related_name="emprestimo_livro")

    def __str__(self):
        return   " Data de Emprestimo: " + str(self.data_emp) + " Livro:" + self.livro.titulo 
