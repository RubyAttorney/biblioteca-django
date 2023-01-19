from django.db import models
import uuid
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os
# Create your models here.
class Editora(models.Model):
    nome = models.CharField("Nome", max_length=50)

    def __str__(self):
        return self.nome
        
class Livros(models.Model):
    titulo = models.CharField("Titulo", max_length=200)
    descricao = models.TextField("Descrição")
    data = models.DateField(auto_now_add=True)
    quantidade = models.PositiveIntegerField("Quantidade")
    editora = models.ForeignKey(Editora, on_delete=models.DO_NOTHING)

    capa = models.ImageField("Capa", upload_to='dados',width_field='largura',height_field='altura' ,null=True, blank=True)
    largura = models.IntegerField(null=True, blank=True)
    altura = models.IntegerField(null=True, blank=True)

    autor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name="Livro"
        verbose_name_plural="Livros"

@receiver(pre_delete, sender=Livros)
def deletar_livro_imagem(sender, instance, **kwargs):
    if instance.capa:
        if os.path.isfile(instance.capa.path):
            os.remove(instance.capa.path)


class Emprestimo(models.Model):
    codigo = models.UUIDField(default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    data_emp = models.DateField(auto_now_add=True)
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING, related_name="emprestimo_livro")

    def __str__(self):
        return   " Data de Emprestimo: " + str(self.data_emp) + " Livro:" + self.livro.titulo 
