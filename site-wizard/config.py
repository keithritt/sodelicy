import json
from file import File
from pprint import pprint
from ui import UI

class Config:
  def __init__(self):
    print('Config.__init__()')
    self.file = File('data/config.json')
    config_json = self.file.read()


    if config_json == '':
      self.all = {}
    else:
      self.all = json.loads(config_json)

    #pprint(self.all)
    #pprint(self.all.keys())

    if 'domains' not in self.all.keys():
      UI.print('domains does not exist in config - creating it');
      self.all['domains'] = {}

    #if 'ports' not in self.all.keys():
    #  UI.print('ports does not exist in config - creating it');
    #  self.all['ports'] = {}

    #pprint(self.all)




  def save(self):
    #self.file.write(json.dumps(self.all), 'w')
    self.file.write(json.dumps(self.all, indent=4, sort_keys=True), 'w')
    #json.dumps(parsed)

  '''
format of config
ports:
  8000: DOMAIN:gadake
  8001: DOMAIN:keithandjess

domains:
  gadake:
    domain-id: 1
    port: 8000
    domain: gadake.com
    dbms: mysql
    git-repo:

  sodelicy:
    domain-id: 2
    port: 8019
    domainL sodelicy.com
    dbms: mysql
    git-repo: https://github.com/keithritt/gadake.git

repos:
 - think this needs to be moved a database


  '''