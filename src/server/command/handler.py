# -*- coding: utf-8 -*-

class Handler():
  def __init__(self):
    self.stream = ''

  def onReceive(self, aStream):
    self.stream = aStream
  # TODO
    return None, 0

