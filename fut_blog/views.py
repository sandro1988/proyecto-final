from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from fut_blog.models import Post, Avatar, Post, Mensaje
from fut_blog.forms import UsuarioForm
from django.contrib.auth.admin import User



# Create your views here.
def index(request):
    posts = Post.objects.order_by('-publicado_el').all()
    return render(request, "fut_blog/index.html", {"posts": posts})

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
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('fut-blog-login')

class UserLogin(LoginView):
    template_name = 'registration/login.html'
    next_page = reverse_lazy('fut-blog-listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('fut-blog-login')

# FUTBLOG AVATAR

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy('fut-blog-listar')

# ACTUALIZACION DE INFO

class UserActualizar(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('fut-blog-listar')

# MENSAJERIA

class MensajeDetalle(DetailView):
    model = Mensaje

class MensajeListar(ListView):
    model = Mensaje
    
class MensajeCrear(CreateView):
    model = Mensaje
    success_url = reverse_lazy("fut-blog-mensajes-crear") 
    fields = ['nombre', 'email', 'texto']
    

class MensajeBorrar(DeleteView):
    model = Mensaje
    success_url = reverse_lazy("fut-blog-mensajes-listar")

# ABOUT
def about(request):
    return render(request, 'fut_blog/about.html')