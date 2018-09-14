#!/usr/bin/env python
from app import app
import os
  # needed for Heroku:
  # check if a port is defined in an env varibale (e.g. by Heroku)
  # otherwise set to 5000 (local host)
  # define the host is also needed
myPort = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0',debug=True, port=myPort)
