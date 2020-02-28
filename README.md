# Blog app
Blog auto administable con curriculum auto generado en base a las categorias/posts, con contacto y redes sociales

# Cómo empezar

Se requiere servidor Linux con Nginx y Gunicorn

## Instalacíon/Deploy
>##### *Esto fue probado en Digital Ocean con Linux Ubuntu 18.04*

En caso de que el servidor haya sido recién levantado

```
sudo apt-get update -y && sudo apt-get upgrade -y
```
> Recomiendo no tener instalado previamente Apache para prevenedir cualquier incoveniente

Instalación de las librerías básicas requeridas
```
sudo apt install build-essential -y
sudo apt-get install mysql-server -y
sudo apt-get install libmysqlclient-dev -y
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl -y
sudo apt install gunicorn -y
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
```

En caso de usar la configuración de base de datos ya integrada
```
mysql
create user 'django'@'localhost' identified by 'django_art_blog2020';
grant usage on *.* to 'django'@'localhost';
create database art_blog;
grant all privileges on art_blog.* to 'django'@'localhost';
flush privileges;
```
Se recomienda crear un nuevo usuario con accesso SSH
```
adduser <user>
usermod -aG sudo <user>
```

En caso de tener Firewall activo

```
ufw allow OpenSSH
```

>En caso de no tener conocimientos de configuración sobre ufw
>```
>ufw disable
>```

Sincronizar el nuevo usuario para acceder a SSH

```
rsync --archive --chown=<user>:<user> ~/.ssh /home/<user>
```

Una vez creado el usuario está listo, con posibilidad de acceder con SSH, pero recomiendo proseguir como root

```
cd /home/<user>
```
Clonamos el repositorio
```
git clone https://github.com/pmunozroa/blog_autoadministrable.git
```
>Recomiendo hacer un cambio de permisos para evitar problemas más adelante
>```
>chmod 755 -R /home/<user>
>```

Accedemos

```
cd blog_autoadministrable/
```
Creamos un entorno virtual de Python para evitar conflictos con futuros proyectos y dependencias de módulos
```
virtualenv <nombre_entorno>
```
Activamos el entorno
```
source <nombre_entorno>/bin/activate
```
Instalamos los paquetes necesarios
```
pip install django gunicorn psycopg2-binary
pip install -r requirements.txt
```
Una vez todo listo
###Haciendo las pruebas básicas
```
python manage.py migrate
```
Probamos que el proyecto corra sin problemas
```
python manage.py runserver 0.0.0.0:8000
```
>*En este punto, el proyecto debería ser accesible remotamente usando la IP del servidor :8000*

Ahora probamos usando Gunicorn
```
gunicorn --bind 0.0.0.0:8000 art_blog.wsgi
```
>*Lo mismo que lo anterior, si todo funciona, el servidor debería seguir siendo accesible, aunque esta vez sin estilos*

Salimos del ambiente virtual
```
deactivate
```
# Levantando el socket Gunicorn y Nginx
## Gunicorn
Configuración del socket
```
sudo nano /etc/systemd/system/gunicorn.socket
```
Añadimos lo siguiente y guardamos
```
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```
Configuración del servicio
```
sudo nano /etc/systemd/system/gunicorn.service
```
Añadimos lo siguiente y guardamos
```
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=<user>
Group=www-data
WorkingDirectory=/home/<user>/blog_autoadministrable
ExecStart=/home/<user>/blog_autoadministrable/art_blog_env/bin/gunicorn \
        --access-logfile - \
        --workers 3 \
        --bind unix:/run/gunicorn.sock \
        art_blog.wsgi:application
[Install]
WantedBy=multi-user.target
```
Iniciamos el socket y activamos el servicio
```
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl status gunicorn.socket
```
Comprobamos que se haya generado el socket
```
file /run/gunicorn.sock
#output:
/run/gunicorn.sock: socket
```
Comprobamos el estado de Gunicorn
```
sudo systemctl status gunicorn
```
Deberia aparecer dead (inactive)
Probamos a ver si responde
```
curl --unix-socket /run/gunicorn.sock localhost
```
>*Deberia retornar la página de inicio, si no devuelve nada, aún no es necesario preocuparse*

Volvemos a comprobar el estado de Gunicorn
```
sudo systemctl status gunicorn
```
>*Esta vez debería estar Activo y en el Log aparecería el último request*

## Nginx
Creamos la configuración del sitio para que responda el puerto 80
```
sudo nano /etc/nginx/sites-available/<nombre-sitio>
```
Añadimos lo siguiente
```
server {
    listen 80;
    server_name <IP SERVER>;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/<user>/blog_autoadministrable;
    }
    location /media/ {
        root /home/<user>/blog_autoadministrable;
    }
    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```
Creamos el symbolic link
```
sudo ln -s /etc/nginx/sites-available/<nombre-sitio> /etc/nginx/sites-enabled
```
Probamos la configuración esté bien
```
sudo nginx -t
```
Reiniciamos Nginx para que tome la última configuración
```
sudo systemctl restart nginx
```
Ya con esto, la página deberia ser accesible desde cualquier parte solamente poniendo la ip del servidor, sin el puerto, queda a su elección si poner el dominio, HTTPS y SSL

# Ante cualquier cambio, ejecutar los siguientes comandos
Cambios en el proyecto
```
sudo systemctl restart gunicorn
```
Cambios en el Gunicorn, daemon o socket
```
sudo systemctl daemon-reload
sudo systemctl restart gunicorn.socket gunicorn.service
```
Cambios en configuración Nginx
```
sudo nginx -t && sudo systemctl restart nginx
```

# Logs
Log del proceso Nginx
```
sudo journalctl -u nginx
```
Log de acceso al sitio Nginx
```
sudo less /var/log/nginx/access.log
```
Log de errores Nginx
```
sudo less /var/log/nginx/error.log
```
Log de aplicación en Gunicorn
```
sudo journalctl -u gunicorn
```
Log del socket Gunicorn
```
sudo journalctl -u gunicorn.socket
```

# Guía original
[DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04)