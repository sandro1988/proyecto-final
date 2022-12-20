from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from ejemplo_dos.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from ejemplo_dos.forms import UsuarioForm


# Create your views here.

def index(request):
    return render(request, "ejemplo_dos/index.html", {})

class PostList(ListView):
    model = Post #ver aca que paso si esto esta bien

class PostDetalle(DetailView):
    model = Post

class PostListar(ListView):
    model = Post
    
class PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("ejemplo-dos-listar") 
    fields = '__all__'

class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("ejemplo-dos-listar")

class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("ejemplo-dos-listar")
    fields = "__all__"

# User creation login y logout
class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('ejemplo-dos-listar')

class UserLogin(LoginView):
    next_page = reverse_lazy('ejemplo-dos-listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('ejemplo-dos-listar')
