# -*- coding: utf-8 -*-

class Handler():
  def __init__(self):
    self.stream = ''     #contiendra le message reçu de la part du serveur
    self.args = []       # la liste d'arguments 

  def onReceive(self, aStream):
    self.stream = aStream
    self.extractArgs()
  # TODO
    return None, 0

  def extractArgs(self):
    self.args = self.stream.split(':')

