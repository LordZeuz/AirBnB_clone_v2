#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static

apt-get update
apt-get -y install nginx
ufw allow "Nginx HTTP"
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
      return 301 https://www.youtube.com/watch?v=32Tz0OnTti4;
   }
   error_page 404 /404.html;
   location = /404.html{
      internal;
   }
}">/etc/nginx/sites-available/default
service nginx restart
