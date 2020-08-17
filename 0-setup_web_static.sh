#!/usr/bin/env bash
# set up servers to deploy web static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared /data/web_static/releases/test
sudo echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -fs /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "41i \\\nlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n}\n" /etc/nginx/sites-available/default
sudo service nginx restart
