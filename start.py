#!/usr/python
# -*- coding: utf-8 -*-

import os
import webbrowser
from subprocess import Popen

# Start the server
server_path = os.path.abspath('src/server/distro_server.py')
server_up = Popen(['python', server_path]) # asynchronous execution, so the script continue and open the browser

# Open the webapp with the default browser
web_path = os.path.abspath('src/webapp/index.html')
url = "file://"+web_path
webbrowser.open(url)
