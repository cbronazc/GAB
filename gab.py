#!/usr/bin/env python2.7
import automerger
import releases
import config
import api

status_code = api.authenticate()
if status_code == 200:
  if config.automerger:
    automerger.run()
  if config.releases:
    releases.run()
else:
  print "Could not authenticate %s"%status_code