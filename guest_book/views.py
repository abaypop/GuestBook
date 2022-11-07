from django.shortcuts import render, get_object_or_404, redirect
from .models import BukuTamu
from .forms import BukuTamuForm
from django.contrib import messages

def index(request):
    posts = BukuTamu.objects.all()
    if request.method == 'POST':
        form = BukuTamuForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil disimpan')
            return redirect('index')
    else:
        form = BukuTamuForm()
    context = {
        "posts": posts,
        "form": form,
    }

    return render(request, "guest_book/index.html", context)