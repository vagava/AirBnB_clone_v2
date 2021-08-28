#!/usr/bin/env bash
# Install nginx web server
# Step 1: Install nginx: Update apt packaging system
if [ ! -x /usr/sbin/nginx ]; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi
# Step 2: Create directories
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
# Step 3: Create fake file HTML
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" > /data/web_static/releases/test/index.html
# Step 4: Create symbolic link, If the symbolic link already exists,
# it should be deleted and recreated every time the script is ran.
ln -sf /data/web_static/releases/test/ /data/web_static/current
# Step 5: Create permissions
sudo chown -R ubuntu:ubuntu /data/
# Step 6: Adding line to configurate server
sed -i '57 i \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
# Step 7: Reload/restart Nginx with nginx command:
# To force close and restart Nginx and related processes
sudo /etc/init.d/nginx restart

