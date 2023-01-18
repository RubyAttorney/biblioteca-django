from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from .models import Emprestimo, Livros
from .forms import LivrosForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    livros = Livros.objects.all()
    return render(request, "home.html", {"livros":livros})

def detalhar_livro(request, id):
    livro = Livros.objects.get(id=id)
    return render(request, "detalhar_livro.html", {"livro":livro})

def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivrosForm(request.POST)
        if form.is_valid():
            form_id = form.save()
            livro = Livros.objects.get(id=form_id.id)
            livro.autor = request.user
            livro.save()
            return redirect('/')
    else:
        form = LivrosForm()
        return render(request, 'cadastrar_livro.html',{'form':form})

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
    return redirect('/historico_emprestimo/')
    
@login_required
def atualizar_livro(request, id):
    livro = get_object_or_404(Livros, pk=id)
    form = LivrosForm(instance=livro)
    if request.method == 'POST':
        form = LivrosForm(request.POST, instance=livro)
        if form.is_valid():
            livro = form.save()
            return redirect('/')
        else:
            return render(request,'atualizar_livro.html',{'livro':livro,'form':form})
    else:
        return render(request, 'atualizar_livro.html',{'livro':livro,'form':form})

def deletar_livro(request,id):
    livro = get_object_or_404(Livros, pk=id)
    livro.delete()
    return redirect('/')

def meus_livros(request):
    livros = Livros.objects.filter(autor= request.user)
    return render(request,'meus_livros.html',{'livros':livros})

