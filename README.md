# proyecto-final
Mi proyecto final


# Actualizacion Primera Entrega

Se creo una aplicacion para consultar tanto una agenda de familiares, un inventario de coches en un concesionario y uno de una inmobiliaria.
Para correr el programa, se deben seguir en cada caso los pasos enumerados a continuacion. El ejemplo se desarrolla para la app de coches, aunque es equivalente en los otros dos:

1-  Abrir VSCode.

2-  En la terminal ejecutar el comando git clone y agregamos la URL de este proyecto (https://github.com/sandro1988/proyecto-final.git)

3-  Seleccionar o crear una carpeta para el programa.

4-  En la terminal ejecutar los siguientes comandos: 
    - python manage.py makemigrations 
    - python manage.py migrate

5- Para correr la app, ejecutar el siguiente comando:
    - python manage.py runserver

6- En un navegador, abrir el local host: http://127.0.0.1:8000/.
En la pagina de inicio se observan las distintas opciones para cada app (panel-familia, panel-coche y panel-departamentos).

7- Para ver el registro del elemento (por ejemplo coches), poner en la url /panel-coche.
Si existen registros apareceran listados en esta página, en caso contrario la página aparecera vacia y se deberan agregarlos (paso 8).

8- Para agregar un resgistro, poner poner en la url /panel-coche/crear.

9- Para eliminar un registro, poner poner en la url /panel-coche/<int:pk>/borrar.

10- Para actualizar un registro, poner poner en la url /panel-coche/<int:pk>/actualizar.

11- Si se desea ver solamente un registro en particular, poner poner en la url /panel-coche/<int:pk>/detalle.

<int:pk> hace referencia al numero de identificacion unico, el cual se puede obtener en la vista panel-coche (paso 7).

Si desea consultar otro registro, reemplazar coche por familiar o departamentos respectivamente.

