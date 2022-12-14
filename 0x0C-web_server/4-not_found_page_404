#!/usr/bin/env bash
# have a custom 404 page
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start
echo "Ceci n'est pas une page" | sudo tee /usr/share/nginx/html/error_404.html
sudo sed -i "30i \\\terror_page 404 /error_404.html;\n\tlocation = /error_404.html {\n\t\troot /usr/share/nginx/html;\n\t\tinternal;\n\t}" /etc/nginx/sites-available/default
sudo service nginx restart
