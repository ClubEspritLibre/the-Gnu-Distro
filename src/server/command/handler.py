# -*- coding: utf-8 -*-

from copy import *
from boot import *

class Handler():
  def __init__(self):
    self.stream = ''     #contiendra le message reçu de la part du serveur
    self.args = []       # la liste d'arguments 

  def onReceive(self, aStream):
    self.stream = aStream
    if(not self.extractArgs()):
      return None, 0

    if(self.args[0] == 'COPY'):
      res = copyDistribution(self.getDistFileName())
      if(res is not None):
        return res, True
      else:
        return "Erreur lors de la copie", True

    elif(self.args[0] == 'BOOT'):
      if(bootDistribution(self.getDistFileName())):
        return "Opération terminée avec succés", True
      else:
        return "Erreur lors de la création de flash bootable ! ", True
      
  # TODO
    return None, 0

  def extractArgs(self):
    self.args = self.stream.split(':')
    return True

  def getDistFileName(self):
    return DISTROS[self.args[1]]




DISTROS = {'UBUNTU':'ubuntu.iso', 'FEDORA':'fedora.iso', 'MINT':'mint.iso'}
