import json
from file import File
from pprint import pprint
from ui import UI


class Ports:

  def __init__(self):
    print('Ports.__init_()')
    self.file = File('data/ports.json')
    self.map = {}
    self.domain = ''
    self.domain_code = ''
    self.set_map()

  def set_map(self):
    print('Ports.set_map()')
    map_json = self.file.read()

    if map_json == '':
      self.map = {}
    else:
      self.map = json.loads(map_json)

  def add_mapping(self, port, domain):
    self.map[port] = domain

  def save(self):
    #todo - add logic to sort by port id before saving
    self.file.write(json.dumps(self.map), 'w')

  def print_map(self):
    #UI.printBar()
    #UI.print('Current Port Mapping:')
    UI.printBar()
    for port, domain in self.map.items():
      print('{}: {}'.format(port, domain))

    UI.printBar()





  #@staticmethod
  def runWizard(self):
    print('Ports.runWizard()')
    #myself = Ports()
    self.print_map()
    return UI.ask_integer('What port would you like to assign to this domain?')



