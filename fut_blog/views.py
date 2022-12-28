from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from fut_blog.models import Post
from fut_blog.forms import UsuarioForm
from fut_blog.models import Avatar


# Create your views here.
def index(request):
    return render(request, "fut_blog/index.html", {})

class PostList(ListView):
    model = Post
    
class PostListar(ListView):
    model = Post  

class PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("fut-blog-listar")
    fields = '__all__'


class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("fut-blog-listar")

class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("fut-blog-listar")
    fields = "__all__"

class PostDetalle(DetailView):
    model = Post

# FUTBLOG REGISTRO

class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registrate/signup.html'
    success_url = reverse_lazy('fut-blog-login')

class UserLogin(LoginView):
    next_page = reverse_lazy('fut-blog-listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('fut-blog-login')

# FUTBLOG AVATARES

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy('fut-blog-listar')
