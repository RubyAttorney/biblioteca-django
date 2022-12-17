from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from .models import Emprestimo, Livros
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    livros = Livros.objects.all()
    emprestimos = Emprestimo.objects.all()
    return render(request, "home.html", {"livros":livros,"emprestimos":emprestimos})

def detalhar_livro(request, id):
    livro = Livros.objects.get(id=id)
    return render(request, "detalhar_livro.html", {"livro":livro})

@login_required
def fazer_emprestimo(request, id):
    emprestimo_livro = get_object_or_404(Livros, pk=id)
    emprestimo = Emprestimo()
    emprestimo.livro = emprestimo_livro
    emprestimo.usuario = request.user
    emprestimo.save()
    livro = Livros.objects.filter(pk=id)
    livro.update(quantidade =models.F('quantidade') - 1)
    return redirect('/')

@login_required
def historico_emprestimo(request):
    emprestimos = Emprestimo.objects.filter(usuario=request.user)
    return render(request, "historico_emprestimo.html", {'emprestimos':emprestimos})

@login_required
def fazer_devolucao(request,id):
    emprestimo = get_object_or_404(Emprestimo, pk=id)
    livro = Livros.objects.filter(pk=emprestimo.livro.id)
    livro.update(quantidade =models.F('quantidade') + 1)
    emprestimo.delete()
    return redirect('/')
    