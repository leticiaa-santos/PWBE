from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm

def livro_read(request):
    if request.method == 'POST':
        livro = livro_filter(request)
    else:
        livro = []
    livros = Livro.objects.all()
    return render(request, 'livro_read.html', {'livros' : livros, 'livro' : livro})

def livro_create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livro_read')
    else:
        form = LivroForm()
    return render(request, 'livro_form.html', {'form' : form})

def livro_update(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('livro_read')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livro_form.html', {'form' : form})

def livro_delete(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('livro_read')
    return render(request, 'confirmar_delete.html', {'livro' : livro})

def livro_filter(request):
    filtro = request.POST.get('livro_filtro')
    print(filtro)
    livro = Livro.objects.filter(titulo__icontains = filtro) | Livro.objects.filter(autores__icontains = filtro) | Livro.objects.filter(ano__icontains = filtro)
    return livro