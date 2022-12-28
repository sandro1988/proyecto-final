"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ejemplo.views import (index, saludar_a, sumar, monstrar_familiares, BuscarFamiliar, AltaFamiliar, ActualizarFamiliar, BorrarFamiliar,
 FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar, FamiliarDetalle,
 CocheList, CocheCrear, CocheBorrar, CocheActualizar, CocheDetalle,
 DepartamentosList, DepartamentosCrear, DepartamentosBorrar, DepartamentosActualizar, DepartamentosDetalle,)
#from ejemplo_dos.views import index, about, PostList, PostCrear
#from ejemplo_dos.views import (PostDetalle, PostListar, PostCrear, PostBorrar, PostActualizar,
                               #UserSignUp, UserLogin, UserLogout,
                               #AvatarActualizar, UserActualizar, MensajeCrear, MensajeListar, MensajeDetalle, MensajeBorrar)

from fut_blog.views import index, about, PostList, PostCrear
from fut_blog.views import (PostDetalle, PostListar, PostCrear, PostBorrar, PostActualizar,
                            UserSignUp, UserLogin, UserLogout,
                            AvatarActualizar, UserActualizar,
                            MensajeCrear, MensajeListar, MensajeDetalle, MensajeBorrar)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('saludar-a/<nombre>/', saludar_a),
    path('sumar/<int:a>/<int:b>/', sumar),
    path('mi-familia/', monstrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()), # NUEVA RUTA PARA BUSCAR FAMILIAR
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()), # NUEVA RUTA PARA BUSCAR FAMILIAR
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('panel-familia/', FamiliarList.as_view()),
    path('panel-familia/crear', FamiliarCrear.as_view()),
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()),
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),
    path('panel-familia/<int:pk>/detalle', FamiliarDetalle.as_view()),
    #----
    path('panel-coche/', CocheList.as_view()),
    path('panel-coche/crear', CocheCrear.as_view()),
    path('panel-coche/<int:pk>/borrar', CocheBorrar.as_view()),
    path('panel-coche/<int:pk>/actualizar', CocheActualizar.as_view()),
    path('panel-coche/<int:pk>/detalle', CocheDetalle.as_view()),

    #----
    path('panel-departamentos/', DepartamentosList.as_view()),
    path('panel-departamentos/crear', DepartamentosCrear.as_view()),
    path('panel-departamentos/<int:pk>/borrar', DepartamentosBorrar.as_view()),
    path('panel-departamentos/<int:pk>/actualizar', DepartamentosActualizar.as_view()),
    path('panel-departamentos/<int:pk>/detalle', DepartamentosDetalle.as_view()),

  
    

    #FUTBLOG APP
    path('fut-blog/', index, name="fut-blog-index"),
    path('fut-blog/listar/', PostList.as_view(), name="fut-blog-listar"),
    path('fut-blog/<int:pk>/detalle/', PostDetalle.as_view(), name="fut-blog-detalle"),
    path('fut-blog/listar/', PostListar.as_view(), name="fut-blog-listar"),
    path('fut-blog/crear/', PostCrear.as_view(), name="fut-blog-crear"),
    path('fut-blog/<int:pk>/borrar/', PostBorrar.as_view(), name="fut-blog-borrar"),
    path('fut-blog/<int:pk>/actualizar/', PostActualizar.as_view(), name="fut-blog-actualizar"),

    #FUTBLOG REGISTRO LOGIN Y LOGOUT
    path('fut-blog/signup/', UserSignUp.as_view(), name = "fut-blog-signup"),
    path('fut-blog/login/', UserLogin.as_view(), name = "fut-blog-login"),
    path('fut-blog/logout/', UserLogout.as_view(), name = "fut-blog-logout"),

    #FUTBLOG AVATARES
    path('fut-blog/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name = "fut-blog-avatars-actualizar"),
    
    # ACT INFO
    path('fut-blog/users/<int:pk>/actualizar/', UserActualizar.as_view(), name = "fut-blog-users-actualizar"),

    # MENSAJERIA
    path('fut-blog/mensajes/crear/', MensajeCrear.as_view(), name = "fut-blog-mensajes-crear"),
    path('fut-blog/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name = "fut-blog-mensajes-detalle"),
    path('fut-blog/mensajes/listar/', MensajeListar.as_view(), name = "fut-blog-mensajes-listar"),
    path('fut-blog/mensajes/<int:pk>/borrar/', MensajeBorrar.as_view(), name = "fut-blog-mensajes-borrar"),

    # ABOUT
    path('fut-blog/about', about, name="fut-blog-about"),

    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


