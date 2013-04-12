# -*- coding: utf-8 -*-

from copy, boot import *

class Handler():
  def __init__(self):
    self.stream = ''     #contiendra le message reçu de la part du serveur
    self.args = []       # la liste d'arguments 

  def onReceive(self, aStream):
    self.stream = aStream
    if(not self.extractArgs()):
      return None, 0

      if(self.args[0] is 'COPY'):
        copy(getDistFileName())

      elif(self.args[0] is 'BOOT'):
        boot(getDistFileName())
      
  # TODO
    return None, 0

  def extractArgs(self):
    self.args = self.stream.split(':')
    return True

  def getDistFileName(self):
    return DISTRO[self.args[1]]




DISTROS['UBUNTU':'ubuntu.iso', 'FEDORA':'fedora.iso', 'MINT':'mint.iso']
