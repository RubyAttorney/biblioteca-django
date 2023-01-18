from django.contrib import admin
from .models import Editora, Livros, Emprestimo
# Register your models here.
class EditoraAdmin(admin.ModelAdmin):
    model = Editora

class LivrosAdmin(admin.ModelAdmin):
    model = Livros

class EmprestimoAdmin(admin.ModelAdmin):
    model = Emprestimo

admin.site.register(Editora, EditoraAdmin)
admin.site.register(Livros, LivrosAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)

