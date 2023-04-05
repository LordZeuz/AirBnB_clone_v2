apt-get update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
service nginx start
