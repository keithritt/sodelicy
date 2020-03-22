from file import File
from config import Config
import json
from pprint import pprint
from ui import UI


class Domain:
  def __init__(self):
    print('Domain.__init__()')
    self.domain = None
    self.domain_code = None
    self.config = Config()
    self.port = None
    #self.repo_name


    #pprint(self.all_configs)

  def __str__(self):
    return 'Domain(domain: {}, domain_code: {}, port: {})'.format(self.domain, self.domain_code, self.port)

    def __repr__(self):
        return {'domain':self.domain, 'domain_code':self.domain_code, 'port': self.port}

  def prompt_for_domain(self):
    #print('Domain.prompt_for_domain()')
    self.domain = 'brewskis.club' #UI.ask('What domain are you working on?')

    pprint(self.config.all['domains'])
    if self.domain not in self.config.all['domains']:
      if not UI.ask_boolean('This domain: {} is not recognized. Is it new?'.format(self.domain)):
        return self.prompt_for_domain()

    self.set_domain()
    return self.domain

  def set_domain(self):
    #print('Domain.set_domain()')
    if self.domain in self.config.all['domains']:
      #print('domain is in all configs')
      self.load_domain_configs()
    else:
      self.config.all['domains'][self.domain] = {}

    self.run_domain_wizard()


  def load_domain_configs(self):
    print('Domain.load_domain_configs')
    #pprint(self.config.all)
    tmp = self.config.all['domains'][self.domain]
    #pprint(tmp)
    self.domain_code = tmp['domain_code']
    self.port = tmp['port']


  def run_domain_wizard(self):
    print('Domain.run_review_domain_wizard()')
    #print('domain code = ')
    #print(self.domain_code)
    '''
    domain-code
    '''
    if self.domain_code is None:
      UI.print('You do not have a domain code set up.')
      self.prompt_for_domain_code()
    elif UI.ask_boolean('"{}" is set to your domain code. Would you like to change it?'.format(self.domain_code)):
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
      self.domain_code = default
    else:
      self.domain_code = UI.ask('What would you like to use for your domain code?')

  def prompt_for_port(self):
    UI.print('Domain.prompt_for_port()');
    #self.print_port_map()
    #if(UI.ask_boolean('Would you like to use {} as your domain code?'.format(default))):
    #  self.domain_code = default
    #else:
    if(True):
      self.port = '8010'#UI.ask('What would you like to use for your port number?')

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
    parts = self.domain.split('.')
    return parts[0]

  def save(self):
    '''#add current config to all configs and write to json file
    current= {}
    #current['domain'] = self.domain
    current['domain_code'] = self.domain_code
    current['port'] = self.port
    self.config.all['domains'][self.domain] = current
    '''
    self.config.all['domains'][self.domain]['domain_code'] = self.domain_code;
    self.config.all['domains'][self.domain]['port'] = self.port;
    #self.config.all['ports'][self.port] = self.domain
    self.config.save();


    #self.file.close()