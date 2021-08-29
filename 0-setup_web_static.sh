#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

if ! [ "$(command -v nginx)" ]
then
        sudo apt-get -y update && apt-get install -y nginx
        sudo service nginx start
fi

if ! [ -d "/data" ]; then sudo mkdir -p /data/; fi
if ! [ -d "/data/web_static/" ]; then sudo mkdir -p /data/web_static/; fi
if ! [ -d "/data/web_static/releases/" ]; then sudo mkdir -p /data/web_static/releases/; fi
if ! [ -d "/data/web_static/shared/" ]; then sudo mkdir -p /data/web_static/shared/; fi
if ! [ -d "/data/web_static/releases/test/" ]; then sudo mkdir -p /data/web_static/releases/test/; fi
echo " simple content, Bash script that sets up your web servers for the deployment of web_static " > sudo /data/web_static/releases/test/index.html
#delete /data/web_static/current
if [ -d "data/web_static/current" ]; then sudo rm -rf /data/web_static/current; fi
#create a symbolic link if curren no exist it create automatically
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# Change permisions
sudo chown -R ubuntu:ubuntu /data/
#Configure nginx
sudo sed -i '37 i \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
