from ubuntu:jammy
# arg -> only set during buildtime
arg DEBIAN_FRONTEND=noninteractive 
# env persists after build time
env TZ="Europe/Berlin"
run apt update && apt install -y apache2 python3 libapache2-mod-wsgi-py3 python3-pip libpython3-dev net-tools vim htop python3-venv locales less

run echo "LANG=C.UTF-8" > /etc/default/locale
# remove # from "#. /" to uncomment the line in the settings which enables using system locales
run sed -i 's/\#\. \//\. \//g' /etc/apache2/envvars
cmd apachectl start && /bin/bash
# Anwendung:
# /var/www und /etc/apache2/sites-enabled müssen als Volume gemountet werden.
# docker run -d -it --rm --name  flask-app-test -p 8080:80 -v "$(pwd)"/work/sites-enabled:/etc/apache2/sites-enabled -v "$(pwd)"/work/www:/var/www flask-test:latest

