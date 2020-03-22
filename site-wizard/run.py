'''
todo
allow for command line arguments to override asking for certain settings
ie --url=brewskis.club --port=8010
record repo id to config settings
add logic to determine if git commands worked or not
have each env checkout is own branch
set up private key for github - cant seem to push to repo currently
check on gunicorn.conf.py - make sure file exists and matches the ports
the django startproject command will create a directory - this directory can act as the git repo
so we need to rearrange some of the timings with creation of the gunicorn.conf.py file and some of
the git commands
figure out issue with static/admin files not working off the bat
note: check on settings in sites-available
idea: create a symlink to the django project folder in the app - so you can easily navigate the source code
ln -s ~/env/lib/python3.6/site-packages/django

commands run to get dev.brewskis.club running
cd ~/brewskis_club/
python -m django --version
cd ~/home/ubuntu
django-admin startproject brewskis_club
git add brewskis_club
git commit -m "initial commit of django code"
git push --set-upstream origin dev # had errors due to 2fa i think

#note if we want to set up a sql or postgres db - we will have to do that here
todo - figure out how to set up a postgres db in ec2
todo always make these commands run full dir path from home
python manage.py migrate
python manage.py createsuperuser

python manage.py startapp web
# add web to installed apps

#get basic homepage working
mkdir web/templates/web
touch web/templates/web/index.html
touch web/urls.py
add path('', include('web.urls')),

#get user authenticaion working
edit brewskisclub/urls.py
path('', include('django.contrib.auth.urls'))






# had to set up dev.brewskis.club at:
https://dcc.godaddy.com/manage/brewskis.club/dns
Type A
Name/Host dev
Value/Points to 3.217.138.252
TTY 1 hour

commands run from pretty printed tutorials
python manage.py startapp entries

need to add these settings
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    '/home/ubuntu/brewkis_club/brewskis_club/static',
]

then create a symlink

 cd /home/ubuntu/brewskis_club/brewskis_club
 ln -s ../staticfiles/ static

 then copy files /admin folder to staticfiles


'''

#import json
from pprint import pprint
#from inspect import getmembers

from ports import Ports
from ui import UI
from domain import Domain
from file import File
from config import Config
from git import Git
#import subprocess

path_base = '/home/ubuntu/'

def check_parent_directory(domain_code):
  if File.exists(path_base+domain_code):
    print('directory exists')
  else:
    print('directory doesnt exist')


if __name__ == '__main__':
  print('''******
  Welcome to the site setup wizard.
  ****''')

  #config = Config()

  domain_obj = Domain()
  domain_obj.prompt_for_domain()
  print('domain set to: '+domain_obj.domain)
  domain_obj.save()

  #print(domain_obj)

  #tmp hack for testing
  #File.delete_folder(path_base+domain_obj.domain_code+'/')
  File.force_folder_existance(path_base+domain_obj.domain_code+'/')

  env = 'dev' #todo - need to move the to a config file
  git_obj = Git(domain_obj.domain_code, env)
  git_obj.run_wizard()

  # create file for nginx
  #output = UI.run('whoami')
  #print(output)
  #todo figure out this permission issue - folder is currently set to 777 as a temp workaround
  #todo - when chaning port # it does not seem to overwrite
  sites_available_file = '/etc/nginx/sites-available/{}'.format(domain_obj.domain_code)
  if not File.exists(sites_available_file):
    File.force_existance(sites_available_file)

    text = '''
server {{
  listen 80;
   server_name {domain} www.{domain};
   access_log  /home/ubuntu/logs/nginx_access.log;

  location /static/ {{
    alias /home/ubuntu/{domain_code}/staticfiles/;
  }}

  location / {{
    proxy_pass http://127.0.0.1:{port};
    proxy_set_header Host $server_name;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  }}
}}'''.format(domain=domain_obj.domain, domain_code=domain_obj.domain_code, port=domain_obj.port)

    file = File(sites_available_file)
    file.write(text, 'w')

    # create a symlink to this newly created file in sites-enabled

    cmd = 'ln -s /etc/nginx/sites-available/{domain_code} /etc/nginx/sites-enabled/{domain_code}'.format(domain_code = domain_obj.domain_code)
    #print(cmd)
    output = UI.run(cmd)
    print(output)

  gunicorn_file = '/home/ubuntu/{}/gunicorn.conf.py'.format(domain_obj.domain_code)
  if not File.exists(gunicorn_file):
    text = '''
bind = '127.0.0.1:{}'
workers = 1
user = "ubuntu"'''.format(domain_obj.port)
    file = File(gunicorn_file)
    file.write(text, 'w')

  log_conf_file = '/etc/supervisor/conf.d/{}.conf'.format(domain_obj.domain_code)
  if not File.exists(log_conf_file):
    text = '''
[program:{domain_code}]
command=/home/ubuntu/env/bin/gunicorn {domain_code}.wsgi:application -c /home/ubuntu/{domain_code}/gunicorn.conf.py
directory=/home/ubuntu/{domain_code}/
user=ubuntu
stderr_logfile = /home/ubuntu/logs/supervisor-err-{domain_code}.log
stdout_logfile = /home/ubuntu/logs/supervisor-out-{domain_code}.log
autorestart=true
redirect_stderr=true'''.format(domain_code=domain_obj.domain_code)
    file = File(log_conf_file)
    file.write(text, 'w')


  # check to see if this repo has django files
  UI.print('Now you will need to manually edit: ALLOWED_HOSTS in settings.py');


  UI.print('And finally, you will need to run these commands in order to restart the server.');
  text = '''
sudo service nginx restart
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start {}'''.format(domain_obj.domain_code)

  UI.print(text)

  print('script complete')




#port = UI.askInteger('What port would you like to use?')
#ports = Ports()
#ports.set_domain(domain)
#port = ports.runWizard()

#ports.add_mapping(port, domain)
#ports.save()

#print('Summary:')
#print('Domain: {}'.format(domain))
#print('Port: {}'.format(port))

#port = 8000

#port_map = {port:domain}





