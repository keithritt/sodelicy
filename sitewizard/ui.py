from util import Util
from pprint import pprint
import sys
import subprocess
#import logging

class UI:

  #@staticmethod
  #def init():
  #  UI.print('UI.init()');
    #todo - force creation of file first
    #logging.basicConfig(filename='logs/mylog.log', level=logging.DEBUG)

  @staticmethod
  def ask(question):
    ret = input(question+' ')
    if ret == 'exit':
      UI.exit()
    return ret

  @staticmethod
  def ask_integer(question):
    ret = UI.ask(question+' ')

    if not Util.isInt(ret):
      UI.print('Please enter an integer.')
      ret = UI.askInteger(question+' ')

    return ret

  @staticmethod
  def ask_boolean(question):
    ret = UI.ask(question+' (y/n)')
    ret = ret.lower()

    if ret in ('y', 'yes'):
      return True

    if ret in ('n', 'no'):
      return False

    # if you are still here you entered an invalid value
    UI.print("Please answer with 'y' or 'n'.")
    return UI.ask_boolean(question)

  @staticmethod
  def print(text):
    print(text)

  @staticmethod
  def print_bar():
    UI.print('**********************')

  @staticmethod
  def exit():
    sys.exit()

  #run a shell command and return the output
  @staticmethod
  def run(cmd, cwd=None):

    print('UI.run({})'.format(cmd))
    #pprint(cmd)
    if cmd == 'exit':
      UI.exit()

    try:
      # ret = subprocess.run(cmd)
      #subprocess.call(['df', '-h'])
      #subprocess.call('du -hs $HOME', shell=True)
      #print('cmd  = {}'.format(cmd))
      #pprint(cmd.split())
      #print('cwd  = {}'.format(cwd))
      #output = str(subprocess.check_output("{}".format(cmd), cwd=cwd))
      output = subprocess.check_output(cmd.split(), cwd=cwd, stderr=subprocess.STDOUT)
      #print(type(output))
      #print('decoding...')
      #print(output.decode())

      output = output.decode().split("\n")

      # remove opening b' and  trailing \n'
      #output = output.replace("b'", '')
      #output = output.replace('b"', '')
      #output = output.replace("\\n'", '')
      #output = output.replace('\n"', '')
      #output = output.split("\n")

      #pprint(completed_process)
      #print('res = ')
      #pprint(completed_process.output)
    #except FileNotFoundError as e:
    #  UI.print("the file wasnt found")
    #  UI.print(e)
    #  pprint(e)

    except subprocess.CalledProcessError as e:
      #UI.print("called process error")
      #UI.print(e.output)
      output = e.output.decode().split("\n")

    except Exception as e:
      #UI.print("generic exception")
      #UI.print(e)
      #pprint(e)
      #print(type(e))
      #print(e.message)
      output = e.output.decode().split("\n")





    return output

