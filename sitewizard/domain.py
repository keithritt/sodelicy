from file import File
from config import Config
import json
from pprint import pprint
from ui import UI


class Domain:
  def __init__(self):
    self.name = None
    self.code = None
    self.config = Config()
    self.port = None
    #self.repo_name


    #pprint(self.all_configs)

  def __str__(self):
    return 'Domain(name: {}, code: {}, port: {})'.format(self.name, self.code, self.port)

  def __repr__(self):
      return {'name':self.name, 'code':self.code, 'port': self.port}

  def prompt_for_domain(self):
    #print('Domain.prompt_for_domain()')
    self.name = 'brewskis.club' #UI.ask('What domain are you working on?')

    pprint(self.config.all['domain_names'])
    if self.name not in self.config.all['domain_names']:
      if not UI.ask_boolean('This domain name: {} is not recognized. Is it new?'.format(self.name)):
        return self.prompt_for_domain()

    self.set_name()
    return self.name

  def set_name(self):
    #print('Domain.set_domain()')
    if self.name in self.config.all['domain_names']:
      #print('domain is in all configs')
      self.load_domain_configs()
    else:
      self.config.all['domains'][self.name] = {}

    self.run_domain_wizard()


  def load_domain_configs(self):
    print('Domain.load_domain_configs')
    #pprint(self.config.all)
    tmp = self.config.all['domains'][self.name]
    #pprint(tmp)
    self.code = tmp['domain_code']
    self.port = tmp['port']


  def run_domain_wizard(self):
    print('Domain.run_review_domain_wizard()')
    #print('domain code = ')
    #print(self.code)
    '''
    domain-code
    '''
    if self.code is None:
      UI.print('You do not have a domain code set up.')
      self.prompt_for_domain_code()
    elif UI.ask_boolean('"{}" is set to your domain code. Would you like to change it?'.format(self.code)):
      #print('ask boolean produced true')
      self.prompt_for_domain_code()

    '''
    domain-code
    '''
    pprint(self.port)
    if self.port is None:
      UI.print('You do not have a port set up.')
      self.prompt_for_port()
    elif UI.ask_boolean('"{}" is set to your port. Would you like to change it?'.format(self.port)):
      self.prompt_for_port()

     # {"sodelicy.com": {"domain_code": "sodelicy", "port": null}}





  def prompt_for_domain_code(self):
    default = self.get_default_domain_code()
    if UI.ask_boolean('Would you like to use {} as your domain code?'.format(default)):
      self.code = default
    else:
      self.code = UI.ask('What would you like to use for your domain code?')

  def prompt_for_port(self):
    UI.print('Domain.prompt_for_port()');
    self.print_port_map()
    if(UI.ask_boolean('Would you like to use {} as your domain code?'.format(default))):
      self.code = default
    else:
    #if(True):
      self.port = UI.ask('What would you like to use for your port number?')

  def print_port_map(self):
    UI.print('Domain.print_port_map()')
    UI.print('port map:')
    pprint(self.config.all.items())

    tmp = {}
    for domain, data in self.config.all.items():
      tmp[domain] = data['port']

    #pprint(tmp)

    for domain, port in tmp.items():
      UI.print(':{} - {}'.format(port, domain))


  def get_default_domain_code(self):
    parts = self.name.split('.')
    return parts[0]

  def save(self):
    '''#add current config to all configs and write to json file
    current= {}
    #current['domain'] = self.name
    current['domain_code'] = self.code
    current['port'] = self.port
    self.config.all['domains'][self.name] = current
    '''
    self.config.all['domains'][self.name]['domain_code'] = self.code;
    self.config.all['domains'][self.name]['port'] = self.port;
    #self.config.all['ports'][self.port] = self.name
    self.config.save();


    #self.file.close()