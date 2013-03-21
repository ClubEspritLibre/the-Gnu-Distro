#!/usr/python
# -*- coding: utf-8 -*-
# Type d'encodage du fichier

# Attention /!\ : 
# Python est très stricte quand il s'agit d'indentation, 
# alors vaut mieux définir un coding-style dès le début.
# On évite les tabulation : 
# 2 Espaces pour un niveau d'indentation.


from simpleWSpy.server import WebSocketServer
from command.handler import Handler


if __name__ == '__main__' :
  handler = Handler()
  ws = WebSocketServer.WebSocket(('localhost', 9999))
  ws.serve_forever(handler)

