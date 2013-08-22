#!/usr/python
# -*- coding: utf-8 -*-

from simpleWSpy.server import WebSocketServer
from command.handler import Handler

if __name__ == '__main__' :
  handler = Handler()
  ws = WebSocketServer.WebSocket(('localhost', 9999))
  ws.serve_forever(handler)

