from django.db import models

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
        return "Titulo: " +self.titulo + "| Autor: " + self.autor.nome + "| Data: " + str(self.data)

    class Meta:
        verbose_name="Livro"
        verbose_name_plural="Livros"

class Emprestimo(models.Model):
    codigo = models.BigIntegerField(auto_created=True)
    usuario = models.CharField("Usuario", max_length=50)
    data_emp = models.DateField("Data de Emprestimo")
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING, related_name="Emprestimo")

    def __str__(self):
        return "Data de Emprestimo: " + str(self.data_emp) + "Usuario: " + self.usuario + "Livro:" + self.livro.titulo