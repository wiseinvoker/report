# Reporting System

Reporting System built with Django for small teams.

## Environment Setup

### Prepare python environment
```
sudo apt-get update
sudo apt-get install python3-pip python-dev mysql-server libmysqlclient-dev
source /pass/to/virtualenv/bin/activate
cd /pass/to/project
pip3 install -r requirements.txt
```
Setup MySQL db user and password and replace database credentials in `settings.py` .
Then migrate database and create admin user for the website.
```
python manage.py migrate
python manage.py createsuperuser
```
### Prepare for uWSGI

You will need to edit `config/uwsgi.ini` file for your environment
```
sudo pip3 install uWSGI==2.0.11.1
```
Edit `/etc/rc.local` and add:
```
cd /pass/to/project
/usr/local/bin/uwsgi --ini /pass/to/project/config/uwsgi.ini
```

### Setting up nginx

Edit nginx configuration file and add followings:

```
upstream report {

	server  127.0.0.1:5001;
}

server {
	
	listen 5000;
	listen [::]:5000;
	
	location / {
		include /etc/nginx/uwsgi_params;
		uwsgi_pass report;
	}
}
```
In order to check, Visit http://youripaddress:5000.