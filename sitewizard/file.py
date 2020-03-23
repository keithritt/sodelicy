from pprint import pprint
from os import path
from pathlib import Path
from ui import UI

import os
import shutil


class File:
  def __init__(self, file):
    #print('File.__init__({})'.format(file))
    self.file_name = file
    # create the file if it doesnt already exist
    if not path.exists(self.file_name):
      Path(self.file_name).touch()

  def open(self, mode):
    #print('File.open({})'.format(mode))
    self.file = open(self.file_name, mode)

  def read(self):
    #print('File.read()');
    self.open('r')
    ret = self.file.read()
    self.close()
    return ret

  def write(self, text, mode='a'):
    print('File.write({})'.format(mode))
    print(text)
    self.open(mode)
    self.file.write(text)
    self.close()

  def close(self):
    #print('File.close()')
    self.file.close()

  @staticmethod
  def exists(file_path):
    #UI.print('File.exists({})'.format(file_path))
    return path.exists(file_path)

  @staticmethod
  def force_existance(file_path):
    if not File.exists(file_path):
      Path(file_path).touch()

  @staticmethod
  def force_folder_existance(folder_path):
    if not File.exists(folder_path):
      os.mkdir(folder_path)

  @staticmethod
  def delete(file_path):
    os.remove(folder_path)

  @staticmethod
  def delete_folder(folder_path):
    shutil.rmtree(folder_path)